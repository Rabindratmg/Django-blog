from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'index.html'


class BlogDetail(DetailView):
    model =Blog
    template_name= 'blog_detail.html'


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'addblog.html'
    fields = '__all__'

class UpdateBlog(UpdateView):
    model = Blog
    template_name = 'updateblog.html'
    fields = '__all__'

class DeleteBlog(DeleteView):
    model = Blog
    template_name= 'delete.html'
    success_url = reverse_lazy('home')