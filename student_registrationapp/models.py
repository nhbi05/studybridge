from django.db import models
from django.contrib.auth.models import AbstractUser
#register your models here
YEAR_CHOICES = [
    (1, 'First Year'),
    (2, 'Second Year'),
    (3, 'Third Year'),
    (4, 'Fourth Year')
]

SEMESTER_CHOICES = [
    (1, 'First Semester'),
    (2, 'Second Semester')
]

COURSE_CHOICES = [
    ('CS', 'Computer Science'),
    ('ENG', 'Engineering'),
    ('MED', 'Medicine'),
    ('BUS', 'Business'),
    ('LAW', 'Law'),
]

class Student(AbstractUser):
    year_of_study = models.IntegerField(choices=YEAR_CHOICES,default=1)
    semester = models.IntegerField(choices=SEMESTER_CHOICES,default=1)
    course = models.CharField(max_length=3, choices=COURSE_CHOICES,default="CS")
    
    def __str__(self):
        return f"{self.username} - {self.get_course_display()}, Year {self.year_of_study}"