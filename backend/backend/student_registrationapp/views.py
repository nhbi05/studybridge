from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import StudentRegistrationForm
# Create your views here.



def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to their personalized dashboard
    else:
        form = StudentRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def dashboard(request):
    # This will show content based on user's course and year
    user = request.user
    context = {
        'course': user.get_course_display(),
        'year': user.get_year_of_study_display(),
    }
    return render(request, 'accounts/dashboard.html', context)