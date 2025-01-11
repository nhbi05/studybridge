from django.urls import path
from .views import note_list, tutorial_list, dashboard_view,user_info

# URLs configuration
from django.urls import path

urlpatterns = [
    path('user/info/', user_info, name='user-info'),
    path('notes/', note_list, name='note-list'),
    path('tutorials/', tutorial_list, name='tutorial-list'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
