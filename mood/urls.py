from django.urls import path
from .views import (MoodReadView,MoodDashboardView,
                    MoodAddView,MoodDeleteView,
                    MoodUpdateView)
urlpatterns=[
    path('',MoodDashboardView.as_view(),name='mood-home'),
    path('create/',MoodAddView.as_view(),name='mood-create'),
    path('<str:pk>/',MoodReadView.as_view(),name='mood-read'),
    path('<str:pk>/update/',MoodUpdateView.as_view(),name='mood-update'),
    path('<str:pk>/delete/',MoodDeleteView.as_view(),name='mood-delete'),
]