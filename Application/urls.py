from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
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
    path('place_bid/<int:post_id>/', views.place_bid, name='place_bid'),  # For placing bids
    path('view_bids/<int:post_id>/', views.view_bids, name='view_bids'),  # For viewing bids
    path('', LogoutView.as_view(next_page='index'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
