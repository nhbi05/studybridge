# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username', 'email', 'course', 'year_of_study', 'password1', 'password2']