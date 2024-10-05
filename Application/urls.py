from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path('custsignup', views.custsignup, name='custsignup'),
    path('workersignup', views.workersignup, name='workersignup'),
]
