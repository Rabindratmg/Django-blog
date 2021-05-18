"""ApiEg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Blog import views as blog_view
from Profile import views as profile_view
from Account import views as account_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",blog_view.Home,name='home'),
    path('profile/',profile_view.Profile, name='profile'),
    path('register/',account_view.create_user, name='register'),
    path('logout/',account_view.logout_user, name='logout'),
    path('login/', account_view.login_user, name='login'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
