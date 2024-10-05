from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path('customer-signup', views.custsignup, name='custsignup'),
    path('worker-signup', views.workersignup, name='workersignup'),
]
