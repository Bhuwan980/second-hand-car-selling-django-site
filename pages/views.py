from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_car = Car.objects.filter(if_featured=True).order_by('-created_date')
    all_car = Car.objects.order_by('-created_date')
    context = {'teams':teams,
                'featured_car': featured_car, 
                'all_car': all_car,
    }
    return render(request, 'pages/home.html',context )

def contact(request):
    return render(request, 'pages/contact.html')
    
def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def car(request):
    return render(request, 'pages/cars.html')
