from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('car/', car, name='car'),
    path('car-detail/<int:id>/', cardetail, name='cardetail'),
    path('car/search/', Search, name='search'), 

    path('accounts/login/', Login, name='login'), 

    path('accounts/register/', Register, name='register'),
    
    path('accounts/logout/', Logout, name='logout'),
    path('inquery/', Contacts, name='inquery')


]