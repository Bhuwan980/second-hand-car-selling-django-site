from django.core import paginator
from pages.admin import CarAdmin
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

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

def cardetail(request, id):
    car = Car.objects.get(pk=id)
   
    
    context={'car':car}
    
    return render(request, 'pages/car-details.html', context)

def contact(request):
    return render(request, 'pages/contact.html')
    
def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def car(request):
    cars = Car.objects.order_by('-created_date')
    # deciding how many car to show
    paginator = Paginator(cars, 1)
    #getting the page number
    page = request.GET.get('page')
    #getting the cars of the above page number
    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)
    # page_obj = paginator.get_page(page)

    context = {
        'cars':page_obj
    }
    return render(request, 'pages/cars.html', context)



def Search(request):
    search = request.GET.get('search_keyword')
    if search:
        search_car = Car.objects.filter(Q(car_title__icontains=search) | Q(description__icontains=search) | Q(model__icontains=search) | Q(color__icontains=search) )

        paginator = Paginator(search_car, 1)
        page = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(1)
        
    context = {
        'page_obj': page_obj, 
        'keyword': search
    }
    return render(request, 'pages/search.html', context)