from typing import Any
from django.views.generic import (CreateView,DetailView,
                                  DeleteView,UpdateView,
                                  ListView)
from .models import MoodData
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from joblib import load
from plotly.offline import plot
import plotly.express as px
import pandas as pd
from .function import get_random_unique_recommendations
# Create your views here.

model_path = 'RMA-EMO.joblib'
model = load(model_path)

class MoodDashboardView(LoginRequiredMixin,ListView):
    template_name='mood/MoodDashboard.html'
    model=MoodData
    context_object_name='Moods'

    def get_queryset(self):
        return MoodData.objects.filter(user=self.request.user).order_by('-dateposted')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        data= MoodData.objects.filter(user=self.request.user)
        
        plot_data=[
            {
            'Moodtype':x.moodtype,
            'DatePosted':x.dateposted,

        } 
        for x in data]
        if not plot_data:
            return context
        else:

            df=pd.DataFrame(plot_data)

            df['DatePosted'] = pd.to_datetime(df['DatePosted'])

            fig = px.line(
                df,
                x='DatePosted',
                y='Moodtype',
                markers='Moodtype',  
                line_shape='linear',  
                category_orders={'Moodtype': ['Excited', 'Happy', 'Fear', 'Sad', 'Angry']}
            )

            # Add rangeselector to enable zooming
            fig.update_layout(
                xaxis=dict(
                    rangeselector=dict(
                        buttons=list([
                            dict(count=1, label="1d", step="day", stepmode="backward"),
                            dict(count=7, label="1w", step="day", stepmode="backward"),
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(step="all")
                        ])
                    ),
                    rangeslider=dict(visible=True),
                    type="date"
                ),
                yaxis_title='Mood Type',
            )
            mood_plot=plot(fig,output_type="div")
            context['mood_plot']=mood_plot

        return context

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
            info_message = 'You might have forgotten to select a value for mood. We have predicted it for you. Check back and edit if need be.'
            messages.info(self.request, info_message)
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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        user_mood = self.get_object().moodtype

        recommendations = get_random_unique_recommendations(user_mood, num_recommendations=3)

        context['recommendations'] = recommendations

        return context

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

