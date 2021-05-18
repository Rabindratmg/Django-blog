from .models import User_Profile
from Account.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Account)
def post_save_create_profile(sender,instance,created,**kwargs):
    if created:
        User_Profile.objects.create(user=instance,first_name=instance.first_name,Email=instance.email)