from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render,redirect
from .form import UserForm,UserUpdateForm
from django.views.generic import CreateView,TemplateView,UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class Homepage(TemplateView):
    template_name='users/Homepage.html'
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            # Redirect authenticated users to MoodDashboardView
            return redirect("mood-home")
        return super().dispatch(request, *args, **kwargs)

class SignUpView(CreateView):
    form_class=UserForm
    template_name='users/signup.html'
    success_url='/login'

class ProfileView(LoginRequiredMixin,UpdateView):
    model=User
    template_name='users/profile.html'
    success_url='/'
    context_object_name='user'
    form_class=UserUpdateForm

    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        return self.request.user
