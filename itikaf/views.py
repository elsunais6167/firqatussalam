from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mosque, Applicant
from django.contrib import messages

import re

date_string = '2022-03-28T18:00:00'
# Create your views here.

def home(request):
    #cities = Lga.objects.all()
    mosques = Mosque.objects.all()
    context = {
        #'cities': cities,
        'mosques': mosques
        }
    return render(request, 'home.html', context)


def apply(request, pk):
    masjids_id = Mosque.objects.get(id=pk)
    masjids_id = str(masjids_id)
    masjid_id = re.sub('[^0-9]', '', masjids_id)
    masjid_id = int(masjid_id)
    context = {
        'masjid_id': masjid_id,
    }
    return render(request, 'apply.html', context)

def application(request):
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

    if request.method =='POST':
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
        #id_image = request.GET.get('id-card')
        #photo = request.Get.get('passport')

        details = Applicant(
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
            #id_image = id_image,
            #photo = photo,

        )
        details.save()
        return HttpResponse('Congratulations. You have successfully applied')
    return render(request, 'home.html')

def dashboard(request):
    context = {

    }

    return render(request, 'applicant.html', context)