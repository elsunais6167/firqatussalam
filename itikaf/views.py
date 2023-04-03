from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, HttpResponseRedirect
from django.urls import reverse

from .models import Mosque, Applicant, Approval, CheckIn, CheckOut, Comment, MosqueAdmin
from .forms import CreateUserForm, Admins

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
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
    masjid_id = title.id
    
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

@login_required
def mosque_dashboard(request):
    mosque_admin = get_object_or_404(MosqueAdmin, user=request.user)
    mosque = mosque_admin.mosque

    list_applicants = Applicant.objects.filter(mosque=mosque)
    total_applicants = list_applicants.count()
    num_applicants_with_approval = Applicant.objects.filter(mosque=mosque, approval__isnull=False).distinct().count()
    num_applicants_with_checkin = Applicant.objects.filter(mosque=mosque, checkin__isnull=False).distinct().count()
    num_applicants_with_checkout = Applicant.objects.filter(mosque=mosque, checkout__isnull=False).distinct().count()
    
    context = {
        'list_applicants': list_applicants,
        'mosque':mosque,
        'total_applicants': total_applicants,
        'num_applicants_with_approval': num_applicants_with_approval,
        'num_applicants_with_checkin': num_applicants_with_checkin,
        'num_applicants_with_checkout': num_applicants_with_checkout,
    }
    return render(request, 'mosque_dashboard.html', context)

@login_required
def applicant_info(request, pk):
    applicant_info = Applicant.objects.get(id=pk)
    applicant_id = applicant_info.id
    
    latest_comment = None
    comments = Comment.objects.filter(participant=applicant_info)
    if comments.exists():
        latest_comment = comments.last()
    
    latest_check_out = None
    check_out = CheckOut.objects.filter(participant=applicant_info)
    if check_out.exists():
        latest_check_out = check_out.last()

    latest_check_in = None
    check_in = CheckIn.objects.filter(participant=applicant_info)
    if check_in.exists():
        latest_check_in = check_in.last()
    
    latest_approved = None
    approved = Approval.objects.filter(participant=applicant_info)
    if approved.exists():
        latest_approved = approved.last()
    
    context = {
        'applicant_info': applicant_info,
        'applicant_id': applicant_id,
        'latest_comment': latest_comment.additional_info if latest_comment else None,
        'latest_check_out': latest_check_out.check_out if latest_check_out else None,
        'latest_check_in': latest_check_in.check_in if latest_check_in else None,
        'latest_approved': latest_approved.approved if latest_approved else None,
      
    }
    return render(request, 'applicant_info.html', context)


@login_required
def comment(request, pk):
    comment = request.POST.get('comment')
    participant = get_object_or_404(Applicant, pk=pk)

    if request.method == "POST":
        additional_info = comment
        participant = participant

        com = Comment(
            participant = participant,
            additional_info = additional_info
        )
        com.save()

        url = reverse('applicant_info', kwargs={'pk': participant.pk})
        return redirect(url)
    context = {
        'participant': participant
    }
    return render(request, 'applicant_info.html', context)


@login_required
def checkout(request, pk):
    check_out = request.POST.get('Checked-Out')
    participant = get_object_or_404(Applicant, pk=pk)


    if request.method == "POST":
        check_out = check_out
        participant = participant
        
        
        cko = CheckOut(
            participant = participant,
            check_out = check_out
        )
        cko.save()

        url = reverse('applicant_info', kwargs={'pk': participant.pk})
        return redirect(url)
    
    context = {
        'participant': participant
    }
    return render(request, 'applicant_info.html', context)


@login_required
def approved(request, pk):
    approved = request.POST.get('Approve')
    participant = get_object_or_404(Applicant, pk=pk)

    if request.method == "POST":
        approved = approved
        participant = participant

        app = Approval(
            participant = participant,
            approved = approved
        )
        app.save()

        url = reverse('applicant_info', kwargs={'pk': participant.pk})
        return redirect(url)

    context = {
        'participant': participant
    }
    return render(request, 'applicant_info.html', context)

@login_required
def checkin(request, pk):
    check_in = request.POST.get('Checked-In')
    participant = get_object_or_404(Applicant, pk=pk)

    if request.method == "POST":
        check_in = check_in
        participant = participant

        chk = CheckIn(
            participant = participant,
            check_in = check_in
        )
        chk.save()

        url = reverse('applicant_info', kwargs={'pk': participant.pk})
        return redirect(url)
    context = {
        'participant': participant
    }
    return render(request, 'applicant_info.html', context)

@login_required
def new_applicant(request):
    #mosque_admin = get_object_or_404(MosqueAdmin, user=request.user)
    #mosque_id = mosque_admin.mosque.id
    #added_by = mosque_admin.id

    if request.method == 'POST':
        # Get the form data
        mosque_admin = get_object_or_404(MosqueAdmin, user=request.user)
        photo = request.FILES.get('passport')
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
        mosque_id = mosque_admin.mosque.id
        added_by = mosque_admin


        # Create the new applicant object
        details = Applicant(
            photo=photo,
            mosque_id=mosque_id,
            name=name,
            age=age,
            address=address,
            phone=phone,
            next_of_kin_name=next_of_kin_name,
            next_of_kin_phone=next_of_kin_phone,
            medical_condition=medical_condition,
            start_date=start_date,
            end_date=end_date,
            id_type=id_type,
            id_card_no=id_card_no,
            id_image=id_image,
            added_by=added_by
        )
        details.save()
        return redirect('mosque_dashboard')

    context = {

    }
    return render(request, 'md_apply.html', context)

@login_required
def update_info(request, pk):
    mosque_id = get_object_or_404(Mosque, id=pk)
    mosque = Mosque.objects.get(id=pk)
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    if request.method == 'POST':
        name = request.POST.get('AName')
        lga = request.POST.get('lga')
        address = request.POST.get('address')
        phone = request.POST.get('phoneNumber')
        accepting_applications = request.POST.get('aa') == 'on'

        mosque.name = name
        mosque.lga = lga
        mosque.address = address
        mosque.phone = phone
        mosque.accepting_applications = accepting_applications
        mosque.save()
        url = reverse('update_info', kwargs={'pk':  mosque_id.pk})
        return redirect(url)
        
   
    context = {
        'profile':  mosque_id,
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,
    }

    return render(request, 'update_info.html', context)

@login_required
def profile(request):
    mosque_admin = get_object_or_404(MosqueAdmin, user=request.user)
    mosque = mosque_admin.mosque

    if request.method == 'POST':
        name = request.POST.get('AName')
        lga = request.POST.get('lga')
        address = request.POST.get('address')
        phone = request.POST.get('phoneNumber')
        accepting_applications = request.POST.get('aa') == 'on'

        mosque.name = name
        mosque.lga = lga
        mosque.address = address
        mosque.phone = phone
        mosque.accepting_applications = accepting_applications
        mosque.save()
        
        return redirect('profile')
    context = {
        'profile': mosque
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

def loggingout(request):
    logout(request)

    return HttpResponseRedirect('/login/')


def login_user(request):
    error_message = ""
    login_error = ""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'mosqueadmin'):
                return redirect('mosque_dashboard')
            elif hasattr(user, 'stateadmin'):
                return redirect('state_admin')
            else:
                error_message = 'Your login details are correct. However, you have not been assigned a Mosque to Manage. Please contact state coordinator'
        else:
            login_error ='Invalid Username or Password, Please Try Again!'
            
    return render(request, 'login.html', {'error_message': error_message, 'login_error': login_error})

@login_required
def user_signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_signup')
    else:
        form = CreateUserForm()
    
    admins = User.objects.all()
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    context = {
        'form': form,
        'admins': admins,
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,

    }
    return render(request, 'user_signup.html', context)

@login_required
def state_admin(request):
    mosques = Mosque.objects.all()
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    context = {
        'mosques': mosques,
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,

        }

    return render(request, 'state_admin.html', context)

@login_required
def add_mosque(request):
    if request.method == 'POST':
        name = request.POST.get('AName')
        lga = request.POST.get('lga')
        address = request.POST.get('address')
        phone = request.POST.get('phoneNumber')
        accepting_applications = request.POST.get('aa') == 'on'

        update_profile = Mosque(
            name = name,
            lga = lga,
            address = address,
            phone = phone,
            accepting_applications = accepting_applications
        )
        # Save the updated profile details
        update_profile.save()
        return redirect('state_admin')
    
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    context = {
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,
    }

    return render(request, 'add_mosque.html', context)

@login_required
def assign_admin(request, pk):
    mosque = get_object_or_404(Mosque, id=pk)
    if request.method == "POST":
        form = Admins(request.POST)
        if form.is_valid():
            admin = form.save(commit=False)
            admin.mosque = mosque
            admin.save()
            return redirect('admin_list')
    else:
        form = Admins(initial={'mosque': mosque})
    
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    context = {
        'form': form,
        'mosque': mosque,
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,
    }

    return render(request, 'assign_admin.html', context)

@login_required
def listUsers(request):
    admins = User.objects.all()
    mosque_admins = MosqueAdmin.objects.all()
    total_approved = Approval.objects.count() 
    total_admins = User.objects.count()
    total_mosques = Mosque.objects.count()

    context = {
        'admins': admins,
        'mosque_admins': mosque_admins,
        'total_approved': total_approved,
        'total_admins': total_admins,
        'total_mosques': total_mosques,
    }
    return render(request, 'listUsers.html', context)