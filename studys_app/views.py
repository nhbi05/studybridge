from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Note, Tutorial
from .serializers import NoteSerializer, TutorialSerializer
#create your views here

@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
