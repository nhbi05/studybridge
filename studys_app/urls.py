from django.urls import path
from . import views



urlpatterns = [
    path('notes/', views.note_list, name='note_list'),
    path('tutorials/', views.tutorial_list, name='tutorial_list'),
]
