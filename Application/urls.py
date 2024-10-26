from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path('customer-signup', views.custsignup, name='custsignup'),
    path('worker-signup', views.workersignup, name='workersignup'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('home/', views.landingpage, name='landingpage'),
]
