"""from rest_framework.routers import DefaultRouter
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = router.urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_student, name='register'),
    path('login/', views.login_student, name='login'),
]