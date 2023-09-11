from django.urls import path
from . import views

urlpatterns = [
    # Organization APIs
    path('banners/', views.BannerApiView.as_view(), name="banner"),
]