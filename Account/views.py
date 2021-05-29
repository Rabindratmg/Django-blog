from django.shortcuts import render, redirect
from .models import Account
from .forms import UserCreationForm, LoginUserForm
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
             return render(request,'home.html',{'forms':form,'error':'paswword didnt match'})
    else:
        form=UserCreationForm()
  
    return render(request,'home.html',{'forms':form})



def logout_user(request):
    logout(request)
    return redirect("home")

def login_user(request):
    user= request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = LoginUserForm(request.POST)
        email=request.POST['email']
        password=request.POST['password']
        user= authenticate(email=email,password=password)
        login(request,user)
        return redirect('home') 
       


    else:
        form=LoginUserForm()
        return render(request,'login.html',{'forms':form})