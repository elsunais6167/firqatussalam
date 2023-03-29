from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mosque, Applicant
from django.contrib import messages

import re

# Create your views here.

def home(request):
    mosques = Mosque.objects.all()
    context = {
        'mosques': mosques
        }
    return render(request, 'home.html', context)


def apply(request, pk):
    title = Mosque.objects.get(id=pk)
    masjids_id = Mosque.objects.get(id=pk)
    masjids_id = str(masjids_id)
    masjid_id = re.sub('[^0-9]', '', masjids_id)
    masjid_id = int(masjid_id)
    context = {
        'masjid_id': masjid_id,
        'title': title
    }
    return render(request, 'apply.html', context)

def application(request):
    photo = request.FILES.get('passport')
    mosque_id = request.POST.get('mos')
    name = request.POST.get('AName')
    age = request.POST.get('age')
    address = request.POST.get('address')
    phone = request.POST.get('phoneNumber')
    next_of_kin_name = request.POST.get('NName')
    next_of_kin_phone = request.POST.get('NphoneNumber')
    medical_condition = request.POST.get('mdcc')
    start_date = request.POST.get('SDate')
    end_date = request.POST.get('EDate')
    request.method = 'POST'
    id_type = request.POST['IdType']
    id_card_no = request.POST.get('IdNum')
    id_image = request.FILES.get('id-card')
    
    if request.method =='POST':
        photo = photo
        mosque_id = mosque_id
        name = name
        age = age
        address = address
        phone = phone
        next_of_kin_name = next_of_kin_name
        next_of_kin_phone = next_of_kin_phone
        medical_condition = medical_condition
        start_date = start_date
        end_date = end_date
        id_type = id_type
        id_card_no = id_card_no
        id_image = id_image
        

        details = Applicant(
            photo = photo,
            mosque_id = mosque_id,
            name = name,
            age = age,
            address = address,
            phone = phone,
            next_of_kin_name = next_of_kin_name,
            next_of_kin_phone = next_of_kin_phone,
            medical_condition = medical_condition,
            start_date = start_date,
            end_date = end_date,
            id_type = id_type,
            id_card_no = id_card_no,
            id_image = id_image,
            
        )
        details.save()
        request.session['applicant_id'] = details.id
        return redirect('printout')
    
    return render(request, 'home.html')

def mosque_dashboard(request):
    list_applicants = Applicant.objects.all()
    context = {
        'list_applicants': list_applicants
    }
    return render(request, 'mosque_dashboard.html', context)

def applicant_info(request, pk):
    applicant_info = Applicant.objects.get(id=pk)
    #mosque_name = Mosque.objects.get(id=pk)
    context = {
        'applicant_info': applicant_info,
        #'mosque_name': mosque_name,
    }
    return render(request, 'applicant_info.html', context)

def new_applicant(request):
    context = {
        
        }
    return render(request, 'md_apply.html', context)

def profile(request):
    context = {

    }
    return render(request, 'md_profile.html', context)

def printout(request):
    applicant_id = request.session.get('applicant_id')
    if not applicant_id:
        messages.error(request, 'No applicant ID found.')
        return redirect('home')

    try:
        applicant_info = Applicant.objects.get(id=applicant_id)
    except Applicant.DoesNotExist:
        messages.error(request, 'Applicant not found.')
        return redirect('home')
    context = {
        'applicant_info': applicant_info
    }
    return render(request, 'printout.html', context)