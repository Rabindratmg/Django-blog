from django.shortcuts import render, redirect
from .models import Account
from .forms import UserCreationForm
from django.http import request
from django.contrib.auth import login, authenticate,logout


# Create your views here.
def create_user(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password2')
            account= authenticate(email=email,password=password)
            login(request,account)
            return redirect('home')
        else:
             form=UserCreationForm()

    
    else:
        form=UserCreationForm()
        return render(request,'home.html',{'forms':form})



def logout_user(request):
    logout(request)
    return redirect("home")

def login_user(request):
    pass
    return redirect("home")