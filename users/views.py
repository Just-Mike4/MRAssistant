from django.shortcuts import render
from .form import UserForm
from django.views.generic import CreateView,TemplateView,DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Homepage(TemplateView):
    template_name='users/Homepage.html'

class SignInView(CreateView):
    form_class=UserForm
    template_name=''
    success_url='mood-home'

class ProfileView(LoginRequiredMixin,DetailView):
    model=User
    template_name=''