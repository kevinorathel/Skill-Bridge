from django.conf import settings
from django.shortcuts import render, redirect
from .forms import CustomerSignUp
from .forms import SpecialistSignUp
from django.contrib import messages
from django.contrib.auth import login
from .forms import LoginForm
from .models import User


def index(request):
    return render(request, 'Application/index.html')

def clientSignup(request):
    if request.method == 'POST':
        form = CustomerSignUp(request.POST)
        if form.is_valid():
            # print("Form is valid")
            # print(form.cleaned_data)
            user = form.save(commit=False)

            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']

            user.save()
            login(request)
            return redirect('login')
        else:
            # print("Form is invalid")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerSignUp()

    return render(request, 'Application/client-signup.html', {'form': form})

def specialistSignup(request):
    if request.method == 'POST':
        form = SpecialistSignUp(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print("Form is invalid", form.errors)
            form = SpecialistSignUp()
    else:
        form = SpecialistSignUp()
    return render(request, 'Application/specialist-signup.html', {'form': form})

def landingpage(request):
    username = request.session.get('username')
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('login')

    user_data = {
        'username': user.username,
        'firstName': user.first_name,
        'lastName': user.last_name,
        'profile_picture_url': user.profile_picture,
    }

    return render(request, 'Application/landing-page.html', {
        'user_data': user_data,
        'MEDIA_URL': settings.MEDIA_URL
    })



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)

                # Store user details in the session
                # request.session['user_id'] = user.id
                request.session['username'] = username
                # request.session['profile_picture_url'] = user.profile_picture.url if user.profile_picture else None

                return redirect('landingpage')  # Redirect to the landing page
            except User.DoesNotExist:
                messages.error(request, 'User not found')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'Application/login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # token = default_token_generator.make_token(user)
            # reset_link = request.build_absolute_uri(f"/reset_password/{user.pk}/{token}/")
            # send_mail(
            #     'Password Reset Request',
            #     f'Click the link to reset your password: {reset_link}',
            #     'noreply@example.com',
            #     [email]
            # )
            messages.success(request, 'Reset link sent!')
        else:
            messages.error(request, 'User not found')
        return redirect('login')  # Redirect back to the login page

def my_profile(request):
    username = request.session.get('username')

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('login')

    if(user.type == 1):

        user_data = {
            'username': user.username,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'profile_picture_url': user.profile_picture,
            "phone_no": user.phone_no,
            'email': user.email,
            'address': user.address,
            'zipcode': user.zipcode,

        }

        return render(request, 'Application/client-my-profile.html', {
            'user': user_data,
            'MEDIA_URL': settings.MEDIA_URL
        })

    elif(user.type == 2):

        user_data = {
            'username': user.username,
            'firstName': user.first_name,
            'lastName': user.last_name,
            'profile_picture_url': user.profile_picture,
            "phone_no": user.phone_no,
            'email': user.email,
            'address': user.address,
            'zipcode': user.zipcode,
            'date_of_birth': user.date_of_birth,
            'gender': user.gender,
            'experience_level': user.experience_level,
            'languages_spoken': user.languages_spoken,
            'linkedin_profile': user.linkedin_profile,
            'skill_category': user.skill_category,
            'qualification': user.qualification,
            'availability': user.availability,
            'willing_to_relocate': user.willing_to_relocate
        }

        return render(request, 'Application/specialist-my-profile.html', {
            'user': user_data,
            'MEDIA_URL': settings.MEDIA_URL
        })
