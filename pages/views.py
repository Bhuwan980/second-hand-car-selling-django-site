from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    context = {'teams':teams}
    return render(request, 'pages/home.html',context )

def contact(request):
    return render(request, 'pages/contact.html')
    
def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def car(request):
    return render(request, 'pages/cars.html')
