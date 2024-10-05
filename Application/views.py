from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'Application/index.html')

def login(request):
    return render(request, 'Application/login.html')

def custsignup(request):
    return render(request, 'Application/custsignup.html')

def workersignup(request):
    return render(request, 'Application/workersignup.html')
