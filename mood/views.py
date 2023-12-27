from django.shortcuts import render
from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class MoodDashboardView(LoginRequiredMixin,ListView):
    template_name=''
    model=MoodData
    

class MoodAddView(LoginRequiredMixin,CreateView):
    template_name=''
    model=MoodData
    fields=['moodtype','description']
    success_url='mood-home'

class MoodReadView(LoginRequiredMixin,DetailView):
    template_name=''
    model=MoodData

class MoodDeleteView(LoginRequiredMixin,DeleteView):
    template_name=''
    model=MoodData
    success_url='mood-home'

class MoodUpdateView(LoginRequiredMixin,UpdateView):
    template_name=''
    model=MoodData
    fields=['moodtype','description']
    success_url='mood-home'

