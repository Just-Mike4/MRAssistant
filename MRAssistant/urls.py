"""MRAssistant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from users.views import Homepage,SignInView,ProfileView

urlpatterns = [path("admin/", admin.site.urls),
               path("home/", include("mood.urls")),
               path('',Homepage.as_view(),name='homepage'),
               path('signin/',SignInView.as_view(),name='signin'),
               path('login/',LoginView.as_view(),name='login'),
               path('logout/',LogoutView.as_view(),name='logout'),
               path('profile/',ProfileView.as_view(),name='profile'),
               ]
