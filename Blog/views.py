from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView,UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
class Home(ListView):
    model = Blog
    template_name = 'index.html'


class BlogDetail(DetailView):
    model =Blog
    template_name= 'blog_detail.html'


class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'addblog.html'
    fields = ['title','description','blog_images']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid (form)
    


class UpdateBlog(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'updateblog.html'
    fields = ['title','description','blog_images']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid (form)
    
    def test_func(self):
        blog=self.get_object()
        if self.request.user== blog.author:
            return True
        return False




class DeleteBlog(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        blog=self.get_object()
        if self.request.user== blog.author:
            return True
        return False