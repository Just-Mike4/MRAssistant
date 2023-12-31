from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import redirect
from .form import UserForm,UserUpdateForm
from django.views.generic import CreateView,TemplateView,UpdateView
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# Create your views here.

class Homepage(TemplateView):
    template_name='users/Homepage.html'
    
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("mood-home")
        return super().dispatch(request, *args, **kwargs)

class SignUpView(CreateView,SuccessMessageMixin):
    form_class=UserForm
    template_name='users/signup.html'
    success_url = reverse_lazy('login')
    success_message='User Account Created, You Can Now Login'

    def form_valid(self, form):
        response = super().form_valid(form)
        
        return response

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("mood-home")
        return super().dispatch(request, *args, **kwargs)

class LogInView(LoginView):
    template_name='users/login.html'

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect("mood-home")
        return super().dispatch(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model=CustomUser
    template_name='users/profile.html'
    success_url='/profile'
    context_object_name='user'
    form_class=UserUpdateForm
    success_message='Profile Updated Successfully'

    def form_valid(self, form):
        form.instance = self.request.user
        return super().form_valid(form)
    
    def get_object(self, queryset=None):
        return self.request.user

