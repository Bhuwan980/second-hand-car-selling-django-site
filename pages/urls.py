from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('car/', car, name='car'),

]