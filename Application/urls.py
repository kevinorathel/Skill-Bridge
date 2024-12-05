from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [

    path("", views.index, name="index"),
    path('login', views.login, name='login'),
    path('customer-signup', views.clientSignup, name='custsignup'),
    path('worker-signup', views.specialistSignup, name='workersignup'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('my-profile/<str:username>/', views.my_profile, name='my_profile'),
    path('home/', views.landingpage, name='landingpage'),
    path('create_post/', views.create_post, name='create_post'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
