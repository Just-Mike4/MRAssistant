from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
# Create your views here.


class MoodDashboardView(LoginRequiredMixin,ListView):
    template_name='mood/MoodDashboard.html'
    model=MoodData
    context_object_name='Mood'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("-dateposted")
    
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

