from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from .models import Note
# Create your views here.

def list_notes(request):
    notes = Note.objects.all()
    return render(request, 'study_app/notes.html', {'notes': notes})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('list_notes')
        else:
            return render(request, 'study_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'study_app/login.html')
