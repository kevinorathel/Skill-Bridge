from django.shortcuts import render
from django.http import HttpResponse
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

