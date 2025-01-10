from django.urls import path
from .views import register_student, login_student,logout_student

urlpatterns = [
    path('register/', register_student, name='register'),
    path('login/', login_student, name='login'),
    path('logout/', logout_student, name='login'),
]
