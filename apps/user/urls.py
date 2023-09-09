from django.urls import path
from . import views

urlpatterns = [
    # Organization APIs
    path('invitation/create', views.InivitationApiView.as_view(), name="invitation"),
    path('invitaion/', views.InvitationApiView.as_view(), name="invitation-list"),
    path('invitation/<int:pk>/', views.InivitationRetrieveUpdateDestroyAPIView.as_view(), name="invitation-detail"),

    # Forum APIs
    path('user/create', views.UserCreateApiView.as_view(), name="user-create"),
    path('user/', views.UserApiView.as_view(), name="user-list"),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name="user-detail"),



]
