from django.urls import path
from . import views

urlpatterns = [
    # Organization APIs
    path('organizations/', views.OrganizationApiView.as_view(), name="organization"),
    path('organization/<int:pk>/', views.OrganizationDetailApiView.as_view(), name="organization-detail"),

    # Forum APIs
    path('forum/create', views.ForumCreateApiView.as_view(), name="forum-create"),
    path('forums/', views.ForumApiView.as_view(), name="forum-list"),
    path('forum/<int:pk>/', views.ForumDetailApiView.as_view(), name="forum-detail"),

    # ForumProject APIs
    path('forum-project/create', views.ForumProjectCreateApiView.as_view(), name="forum-project-create"),
    path('forum-projects/', views.ForumProjectListApiView.as_view(), name="forum-project-list"),
    path('forum-project/<int:pk>/', views.ForumProjectDetailApiView.as_view(), name="forum-project-detail"),

    # Event APIs
    path('event/create', views.EventCreateApiView.as_view(), name="event-create"),
    path('events/', views.EventApiView.as_view(), name="event-list"),
    path('event/<int:pk>/', views.EventDetailApiView.as_view(), name="event-detail"),

    # EventTime APIs
    path('event-times/', views.EventTimeApiView.as_view(), name="event-time"),
    path('event-time/<int:pk>/', views.EventTimeDetailApiView.as_view(), name="event-time-detail"),

]
