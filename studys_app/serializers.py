from rest_framework import serializers
from .models import Note, Tutorial, CourseUnit

class CourseUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseUnit
        fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note  # Can be switched to Tutorial or Resource for different resource types
        fields = '__all__'

class NoteSerializer(ResourceSerializer):
    class Meta(ResourceSerializer.Meta):
        model = Note

class TutorialSerializer(ResourceSerializer):
    class Meta(ResourceSerializer.Meta):
        model = Tutorial
