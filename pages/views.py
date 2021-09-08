from django.contrib import auth
from django.core import paginator
from pages.admin import CarAdmin
from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    teams = Teams.objects.all()
    featured_car = Car.objects.filter(if_featured=True).order_by('-created_date')
    all_car = Car.objects.order_by('-created_date')
    # search_model = Car.objects.values('model', 'year', 'city', 'body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    context = {'teams':teams,
                'featured_car': featured_car, 
                'all_car': all_car,
                # 'search_model': search_model
                'model_search': model_search,
                'city_search': city_search, 
                'year_search': year_search, 
                'body_style_search': body_style_search               
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
        search_car = Car.objects.filter(Q(car_title__icontains=search) | Q(description__icontains=search) | Q(model__icontains=search) | Q(color__icontains=search) | Q(year__icontains=search) | Q(city__icontains=search)| Q(body_style__icontains=search) )

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


def Login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None: 
            login(request, user)
            messages.info(request, "Welcome " + username)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            

    context={

    }
    return render(request, 'pages/login.html', context)

def Register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        print(first_name, '____________________________')
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already exist!!')
                return redirect('register')
            
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                login(request, user)
                messages.info(request, 'Welcome to the car zone '+username)
                return redirect('home')
        else:
            messages.info(request, 'Password didn\'t match!!!')
            return redirect('register')

    else:        
        return render(request, 'pages/register.html')

def Logout(request):
    logout(request)
    return redirect('home')
