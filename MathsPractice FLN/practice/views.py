

from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def practicehome(request):
    
    return render(request,'practice/practicehome.html')
def practiceQ1(request):
    
    return render(request,'practice/practiceQ1.html')
