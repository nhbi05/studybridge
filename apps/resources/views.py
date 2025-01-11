from functools import wraps
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.utils import timezone
from .models import Note, Tutorial
from .serializers import NoteSerializer, TutorialSerializer

def user_course_filter(view_func):
    """
    Decorator to automatically filter querysets based on user's course, year, and semester
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request.user_filters = {
            'course': request.user.course,
            'year_of_study': request.user.year_of_study,
            'semester': request.user.semester,
        }
        return view_func(request, *args, **kwargs)
    return wrapper

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    try:
        return Response({
            "username": request.user.username,
            "course": request.user.course,
            "year_of_study": request.user.year_of_study,
            "semester": request.user.semester,
            "last_login": request.user.last_login,
            "date_joined": request.user.date_joined
        })
    except AttributeError as e:
        return Response(
            {"error": "User profile incomplete"},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@user_course_filter
def note_list(request):
    """List all notes or create a new note"""
    if request.method == 'GET':
        notes = Note.objects.filter(**request.user_filters)
        
        # Optional filtering
        resource_type = request.query_params.get('type')
        search_query = request.query_params.get('search')
        
        if resource_type:
            notes = notes.filter(resource_type=resource_type)
        if search_query:
            notes = notes.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
            
        serializer = NoteSerializer(notes, many=True)
        return Response({
            'count': notes.count(),
            'results': serializer.data
        })

    if request.method == 'POST':
        # Automatically add user's course info if not provided
        data = {**request.data, **request.user_filters}
        serializer = NoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
@user_course_filter
def tutorial_list(request):
    """List all tutorials or create a new tutorial"""
    if request.method == 'GET':
        tutorials = Tutorial.objects.filter(**request.user_filters)
        
        # Optional filtering
        tutorial_type = request.query_params.get('type')
        upcoming_only = request.query_params.get('upcoming', '').lower() == 'true'
        search_query = request.query_params.get('search')
        
        if tutorial_type:
            tutorials = tutorials.filter(tutorial_type=tutorial_type)
        if upcoming_only:
            tutorials = tutorials.filter(scheduled_time__gte=timezone.now())
        if search_query:
            tutorials = tutorials.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query)
            )
            
        serializer = TutorialSerializer(tutorials, many=True)
        return Response({
            'count': tutorials.count(),
            'results': serializer.data
        })

    if request.method == 'POST':
        data = {**request.data, **request.user_filters}
        serializer = TutorialSerializer(data=data)
        if serializer.is_valid():
            serializer.save(uploaded_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@user_course_filter
def dashboard_view(request):
    """Get a comprehensive dashboard view of notes and tutorials"""
    # Get recent notes
    notes = Note.objects.filter(**request.user_filters)
    recent_notes = notes.order_by('-upload_date')[:5]
    
    # Get upcoming tutorials
    tutorials = Tutorial.objects.filter(**request.user_filters)
    upcoming_tutorials = tutorials.filter(
        scheduled_time__gte=timezone.now()
    ).order_by('scheduled_time')[:5]
    
    # Get counts
    return Response({
        "recent_notes": NoteSerializer(recent_notes, many=True).data,
        "upcoming_tutorials": TutorialSerializer(upcoming_tutorials, many=True).data,
        "counts": {
            "total_notes": notes.count(),
            "total_tutorials": tutorials.count(),
            "upcoming_tutorials": upcoming_tutorials.count()
        }
    })

