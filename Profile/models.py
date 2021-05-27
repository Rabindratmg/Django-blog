from django.db import models
from Account.models import Account

# Create your models here.


class User_Profile(models.Model):
    user=models.OneToOneField(Account,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200, blank=True)
    last_name=models.CharField(max_length=200, blank=True)
    Email=models.EmailField(max_length=60,blank=True)
    phone=models.IntegerField(null=True, blank=True)
    profile_img=models.ImageField(upload_to="Profile", default="profile.png")
    bio=models.TextField(default="Respresentation of bio")
    created=models.DateTimeField(auto_now_add=True)

   