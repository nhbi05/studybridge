from django.apps import AppConfig


class StudentRegistrationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_registrationapp'
from django.apps import AppConfig

class StudentRegistrationAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student_registrationapp'
    verbose_name = 'Student Registration App'