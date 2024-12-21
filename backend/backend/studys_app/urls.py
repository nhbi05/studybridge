from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list_notes, name='list_notes'),
]
