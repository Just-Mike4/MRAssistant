from django.urls import path
from .views import (MoodReadView,MoodDashboardView,
                    MoodAddView,MoodDeleteView,
                    MoodUpdateView)
urlpatterns=[
    path('',MoodDashboardView.as_view(),name='mood-home'),
    path('create/',MoodAddView.as_view(),name='mood-create'),
    path('<str:token>/',MoodReadView.as_view(),name='mood-read'),
    path('<str:token>/update/',MoodUpdateView.as_view(),name='mood-update'),
    path('<str:token>/delete/',MoodDeleteView.as_view(),name='mood-delete'),
]