from django.shortcuts import render
from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


class MoodDashboardView(LoginRequiredMixin,UserPassesTestMixin,ListView):
    template_name=''
    model=MoodData

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False
    
class MoodAddView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    template_name=''
    model=MoodData
    fields=['moodtype','description']
    success_url='mood-read'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False
    
class MoodReadView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    template_name=''
    model=MoodData

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

class MoodDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name=''
    model=MoodData
    success_url='mood-home'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

class MoodUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name=''
    model=MoodData
    fields=['moodtype','description']
    success_url='mood-home'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

