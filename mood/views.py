from django.shortcuts import get_object_or_404
from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse
# Create your views here.


class MoodDashboardView(LoginRequiredMixin,ListView):
    template_name='mood/MoodDashboard.html'
    model=MoodData
    context_object_name='Moods'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("-dateposted")
    
class MoodAddView(LoginRequiredMixin,CreateView):
    template_name='mood/MoodCreate.html'
    model=MoodData
    fields=['moodtype','description']
    context_object_name='moods'
    success_url='/'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class MoodReadView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    template_name='mood/MoodRead.html'
    model=MoodData
    context_object_name='moodr'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

class MoodDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    template_name='mood/MoodDelete.html'
    model=MoodData
    success_url='/'
    context_object_name='moodd'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

class MoodUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    template_name='mood/MoodCreate.html'
    model=MoodData
    fields=['moodtype','description']
    context_object_name='moods'
    success_url='/'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

