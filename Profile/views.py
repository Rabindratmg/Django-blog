from django.shortcuts import render
from django.http import request
from .models import User_Profile

# Create your views here.

def Profile(request):
    profile=User_Profile.objects.all()
    return render(request,'profile.html',{'profile':profile})
