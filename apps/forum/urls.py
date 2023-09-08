from django.urls import path
from . import views



urlpatterns = [
    path('forums/', views.ForumListCreateView.as_view(), name='forum-list'),
    path('projects/', views.ForumProjectListCreateView.as_view(), name='project-list'),
]