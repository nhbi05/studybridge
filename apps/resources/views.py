from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Note, Tutorial
from .serializers import NoteSerializer, TutorialSerializer
from django.contrib.auth.models import AbstractUser



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    return Response({
        "username": request.user.username,
        "course": request.user.course,
        "year_of_study": request.user.year_of_study,
        "semester": request.user.semester,
    })

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.filter(
            course=request.user.course,
            year_of_study=request.user.year_of_study,
            semester=request.user.semester,
        )
        print(f"User course: {request.user.course}") 
        print(f"User year of study: {request.user.year_of_study}") 
        print(f"User semester: {request.user.semester}")
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.filter(
            course=request.user.course,
            year_of_study=request.user.year_of_study,
            semester=request.user.semester,
        )
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_view(request):
    notes = Note.objects.filter(
        course=request.user.course,
        year_of_study=request.user.year_of_study,
        semester=request.user.semester,
    )
    tutorials = Tutorial.objects.filter(
        course=request.user.course,
        year_of_study=request.user.year_of_study,
        semester=request.user.semester,
    )

    notes_data = NoteSerializer(notes, many=True).data
    tutorials_data = TutorialSerializer(tutorials, many=True).data

    return Response({
        "notes": notes_data,
        "tutorials": tutorials_data,
    })
