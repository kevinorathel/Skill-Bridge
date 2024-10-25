from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from .models import User


def index(request):
    return render(request, 'Application/index.html')

def custsignup(request):
    return render(request, 'Application/custsignup.html')

def workersignup(request):
    return render(request, 'Application/workersignup.html')

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
                # If the user is found, return a success message
                return HttpResponse(f'Hello, {user.first_name}!')
            except User.DoesNotExist:
                return HttpResponse('Invalid credentials!', status=401)
    else:
        form = LoginForm()
        return render(request, 'Application/login.html', {'form': form})

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            reset_link = request.build_absolute_uri(f"/reset_password/{user.pk}/{token}/")
            send_mail(
                'Password Reset Request',
                f'Click the link to reset your password: {reset_link}',
                'noreply@example.com',
                [email]
            )
            return JsonResponse({'status': 'success', 'message': 'Reset link sent!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Email not found'})



@login_required
def my_profile(request):
    user = request.user
    return render(request, 'my_profile.html', {'user': user})

