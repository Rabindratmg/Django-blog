from django.db import models
from Account.models import Account
from django.urls import reverse
from django.shortcuts import redirect


# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=200)
    description= models.TextField()
    blog_images=models.ImageField(upload_to="Blog",default="no-blog-images.png")
    author=models.ForeignKey(Account,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

