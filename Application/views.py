from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'Application/index.html')

def login(request):
    return render(request, 'Application/login.html')

def signup(request):
    return render(request, 'Application/signup.html')
