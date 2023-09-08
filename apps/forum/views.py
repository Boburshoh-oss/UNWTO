from rest_framework import generics
from .models import Forum, ForumProject
from .serializers import ForumSerializer, ForumProjectSerializer




class ForumListCreateView(generics.ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ForumProjectListCreateView(generics.ListAPIView):
    queryset = ForumProject.objects.all()
    serializer_class = ForumProjectSerializer
