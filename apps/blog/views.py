from . import serializers
from rest_framework.views import APIView
from rest_framework import generics
from .models import Banner, Connect
# Create your views here.




class BannerApiView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = serializers.BannerSerializer


class ConnectListApiView(generics.ListAPIView):
    queryset = Connect.objects.all()
    serializer_class = serializers.ContactSerializer
