from django.contrib import admin
from .models import CourseUnit, Note, Tutorial
# Register your models here.
admin.site.register(CourseUnit)
admin.site.register(Note)
admin.site.register(Tutorial)