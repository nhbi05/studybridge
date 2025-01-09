from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from .models import Student

# Create your views here.
@api_view(['POST'])
def register_student(request):
    try:
        student = Student.objects.create_user(
            username=request.data['email'],
            email=request.data['email'],
            password=request.data['password'],
            name=request.data['name'],
            year_of_study=request.data['year_of_study'],
            semester=request.data['semester'],
            course=request.data['course']
        )
        print("Student created:", student)
        return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_student(request):
    email = request.data.get('email')
    password = request.data.get('password')
    
    student = authenticate(username=email, password=password)
    if student:
        login(request, student)
        return Response({
            'id': student.id,
            'email': student.email,
            'name': student.name,
            'course': student.get_course_display(),
            'year': student.get_year_of_study_display(),
            'semester': student.get_semester_display()
        })
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)