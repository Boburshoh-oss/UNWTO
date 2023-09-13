from django.urls import path
from . import views

urlpatterns = [
    # Organization APIs
    path('invitation/', views.InivitationApiView.as_view(), name="invitation"),
    path('invitation/check/', views.InvitationCheckApiView.as_view(), name="invitation-check"),
    path('invitation/generate/', views.search, name="search"),
    path('invitation/download/', views.download_invitations, name="download-invitations"),
    path('invitation/<int:pk>/', views.InivitationRetrieveUpdateDestroyAPIView.as_view(), name="invitation-detail"),
    
    # Forum APIs
    path('user/create/', views.UserCreateApiView.as_view(), name="user-create"),
    path('user/', views.UserApiView.as_view(), name="user-list"),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),

]
