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
from django.contrib.auth.views import (LogoutView,PasswordResetView,
                                       PasswordResetConfirmView,PasswordResetDoneView,
                                       PasswordResetCompleteView)
from users.views import Homepage,SignUpView,ProfileView,LogInView
from rest_framework.routers import DefaultRouter
from mood.api_views import MoodDataViewSet,Login,UserRegistrationAPIView
from users.api_views import CustomUserViewset


router=DefaultRouter()
router.register(r'mood',MoodDataViewSet,basename='user_mood')
router.register(r'user',CustomUserViewset,basename='user_profile')

urlpatterns = [path("protectedmoodadmin/", admin.site.urls),
               path("api/",include((router.urls, 'api'))),
               path("api/login",Login.as_view(),name='api-login'),
               path("api/register",UserRegistrationAPIView.as_view(),name='api-register'),
               path("home/", include("mood.urls")),
               path('',Homepage.as_view(),name='homepage'),
               path('signup/',SignUpView.as_view(),name='signup'),
               path('login/',LogInView.as_view(),name='login'),
               path('logout/',LogoutView.as_view(template_name='users/logout.html'),name='logout'),
               path('profile/',ProfileView.as_view(),name='profile'),
               path('password-reset/',
                    PasswordResetView.as_view(template_name='users/password_reset.html'),
                    name='password-reset'),
                path('password-reset/done',
                    PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
                    name='password_reset_done'),
                path('password-reset-confirm/<uidb64>/<token>',
                    PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
                    name='password_reset_confirm'),
                path('password-reset-complete/',
                    PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
                    name='password_reset_complete'),
               ]
