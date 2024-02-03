from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView
from Users.models import Student
from django.contrib import messages
from practice.views import *
from django.shortcuts import redirect, render
from Users.forms import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        user = Student.objects.get(username=user_name,password=password)

        if user:
            
            
            return redirect('practicehome') 
           
        else:
            return HttpResponse("Please use correct id and password")
            

    else:
        return render(request, 'Users/login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# Create your views here.
def index(request):
    
   return render(request,'Users/homepage.html')


def register(request):

    registered = False
    messages=False
    if request.method == "POST":
        user_form = User_Form(data=request.POST)
        c=len(Student.objects.filter(username=request.POST['username'], password=request.POST['password']))
     

        if user_form.is_valid()  and c==0:
           
            user = user_form.save()
            
            user.save()

            

            registered = True
        if c>0:
            messages=True
            
       
    else:

        user_form = User_Form()
        

    return render(request, 'Users/registration.html',
                            {'registered':registered,
                             'user_form':user_form,'messages':messages})


def home(request):
    if request.user.is_authenticated:
        
        if  request.user.is_superuser:
                login(request,request.user)
                return redirect('admin_home')    
        elif request.user.is_staff:
            login(request,request.user)
            return redirect('staff_home')   
            
        else:
            login(request,request.user)
            return redirect('member_home')
    else:
        return redirect('index')

