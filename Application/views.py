from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import CustomerSignUp
from django.contrib import messages
from django.contrib.auth import login

from .forms import LoginForm
from .models import User


def index(request):
    return render(request, 'Application/index.html')

def custsignup(request):
    if request.method == 'POST':
        form = CustomerSignUp(request.POST)
        if form.is_valid():
            user = form.save()
            login(request)
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomerSignUp()

    return render(request, 'Application/custsignup.html', {'form': form})

def workersignup(request):
    return render(request, 'Application/workersignup.html')
def landingpage(request):
    return render(request, 'Application/landing-page.html')
def signup(request):
    return render(request, 'Application/signup.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return redirect('home/')
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

@login_required
def my_profile(request):
    user = request.user
    return render(request, 'my_profile.html', {'user': user})

