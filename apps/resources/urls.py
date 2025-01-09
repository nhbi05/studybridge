from django.urls import path
from .views import note_list, tutorial_list, dashboard_view

urlpatterns = [
    path('notes/', note_list, name='note-list'),
    path('tutorials/', tutorial_list, name='tutorial-list'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
