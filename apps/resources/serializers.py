from rest_framework import serializers
from .models import Note, Tutorial, CourseUnit

class BaseResourceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'

class CourseUnitSerializer(BaseResourceSerializer):
    class Meta(BaseResourceSerializer.Meta):
        model = CourseUnit

class NoteSerializer(BaseResourceSerializer):
    class Meta(BaseResourceSerializer.Meta):
        model = Note

class TutorialSerializer(BaseResourceSerializer):
    class Meta(BaseResourceSerializer.Meta):
        model = Tutorial