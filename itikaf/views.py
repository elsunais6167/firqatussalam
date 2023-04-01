from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse

from .models import Mosque, Applicant, Approval, CheckIn, CheckOut, Comment, MosqueAdmin
from .forms import CreateUserForm

from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.admin.views.decorators import staff_member_required
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
    applicants_id = Applicant.objects.get(id=pk)
    applicants_id = str(applicants_id)
    applicant_id = re.sub('[^0-9]', '', applicants_id)
    applicant_id = int(applicant_id)
    
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
def profile(request):
    mosque_admin = get_object_or_404(MosqueAdmin, user=request.user)
    mosque = mosque_admin.mosque

    mosque_id = mosque_admin.mosque
    mosque_id= str(mosque_id)
    mosque_id = re.sub('[^0-9]', '', mosque_id)
    mosque_id = int(mosque_id)

    if request.method == 'POST':
        name = request.POST.get('AName')
        lga = request.POST.get('lga')
        address = request.POST.get('address')
        phone = request.POST.get('phoneNumber')
        accepting_applications = request.POST.get('aa') == 'on'

        update_profile = Mosque(
            id = mosque_id,
            name = name,
            lga = lga,
            address = address,
            phone = phone,
            accepting_applications = accepting_applications
        )
        # Save the updated profile details
        update_profile.save()
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

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if hasattr(user, 'mosqueadmin'):
                return redirect('mosque_admin')
            elif hasattr(user, 'stateadmin'):
                return redirect('state_admin')
            else:
                # Handle other cases if necessary
                pass
        else:
            messages.success(request, ('Invalid Username or Password, Please Try Again!'))
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def log_out(request):
    logout(request)
    return redirect('login')

@login_required
def user_signup(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Succesful. You are now logged in")
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'user_signup.html', {'form': form})

@login_required
def state_admin(request):

    mosques = Mosque.objects.all()

    context = {
        'mosques': mosques
        }

    return render(request, 'state_admin.html', context)

@login_required
def add_mosque(request):

    context = {

    }

    return render(request, 'add_mosque.html', context)
