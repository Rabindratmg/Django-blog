from django.shortcuts import render
from django.http import request
from .models import Blog

# Create your views here.
def Home(request):
    blogs=Blog.objects.all()
    return render(request,'index.html',{"blogs":blogs})
