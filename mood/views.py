from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from joblib import load
import os

# Create your views here.

model_path = 'RMA-EMO.joblib'
model = load(model_path)

class MoodDashboardView(LoginRequiredMixin,ListView):
    template_name='mood/MoodDashboard.html'
    model=MoodData
    context_object_name='Moods'

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user).order_by("-dateposted")
    
class MoodAddView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    template_name='mood/MoodCreate.html'
    model=MoodData
    fields=['description']
    context_object_name='moods'
    success_url='/'
    success_message='Mood Recorded Successfully'
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        selected_mood = self.request.POST.get('selected_mood', None)
        if selected_mood:
            form.instance.moodtype = selected_mood
        else:
            form.instance.moodtype=model.predict([self.request.POST.get('description', None)])[0]

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

class MoodDeleteView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,DeleteView):
    template_name='mood/MoodDelete.html'
    model=MoodData
    success_url='/'
    context_object_name='moodd'
    success_message='Mood Deleted Successfully'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False

class MoodUpdateView(LoginRequiredMixin,UserPassesTestMixin,SuccessMessageMixin,UpdateView):
    template_name='mood/MoodCreate.html'
    model=MoodData
    fields=['description']
    context_object_name='moodu'
    success_url='/'
    success_message='Mood Updated Successfully'

    def test_func(self) -> bool | None:
        mood = self.get_object()
        if self.request.user == mood.user:
            return True
        return False
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        selected_mood = self.request.POST.get('selected_mood', None)
        if selected_mood:
            form.instance.moodtype = selected_mood
        return super().form_valid(form)

