from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class MyAccountManager(BaseUserManager):
    def create_user(self, email,username,first_name, password=None):
        if not email:
            raise valueError("User must have an email address")
        if not username:
            raise valueError('User must have username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,

        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,username,first_name,password):
        user= self.create_user(
        email=self.normalize_email(email),
        password=password,
        username=username,
        first_name=first_name,
        )
        user.is_admin =True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user






# Create your models here.
class Account(AbstractBaseUser):
    email= models.EmailField(verbose_name="email",  max_length=60, unique=True)
    username=models.CharField(max_length=120, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now= True)
    is_admin =  models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff =  models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200,blank=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True