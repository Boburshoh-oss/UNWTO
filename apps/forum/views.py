from django.db.models import F
from rest_framework.pagination import PageNumberPagination
from apps.forum.utils.list_api_view import MyListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from . import models, serializers


class PaginationReport(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = "page_size"
    max_page_size = 100


# Organizations Apis
class OrganizationApiView(ListCreateAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    pagination_class = PaginationReport


class OrganizationDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


# Forum Apis
class ForumApiView(MyListAPIView):

    def get_queryset(self):
        limit = int(self.request.GET.get("limit", 10))
        queryset = models.Forum.objects.all()[:limit]
        queryset = queryset.annotate(
            organization_title=F('organization__title'),
            organization_id=F('organization__id')
        )
        return queryset

    serializer_class = serializers.ForumSerializer
    pagination_class = PaginationReport


class ForumCreateApiView(CreateAPIView):
    queryset = models.Forum.objects.all()
    serializer_class = serializers.ForumSerializer


class ForumDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Forum.objects.all()
    serializer_class = serializers.ForumSerializer


# ForumProject Apis
class ForumProjectListApiView(MyListAPIView):
    queryset = models.ForumProject.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            forum_title=F('forum__title')
        )
        return queryset

    serializer_class = serializers.ForumProjectSerializer
    pagination_class = PaginationReport


class ForumProjectCreateApiView(CreateAPIView):
    queryset = models.ForumProject.objects.all()
    serializer_class = serializers.ForumProjectSerializer


class ForumProjectDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.ForumProject.objects.all()
    serializer_class = serializers.ForumProjectSerializer


# Event Apis
class EventApiView(MyListAPIView):
    queryset = models.Event.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            forum_title=F('forum__title')
        )
        return queryset

    serializer_class = serializers.EventSerializer


class EventCreateApiView(CreateAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


class EventDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer


# EventTime Apis
class EventTimeApiView(ListCreateAPIView):
    queryset = models.EventTime.objects.all()
    serializer_class = serializers.EventTimeSerializer
    pagination_class = PaginationReport


class EventTimeDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.EventTime.objects.all()
    serializer_class = serializers.EventTimeSerializer
from rest_framework import generics
from .models import Forum, ForumProject
from .serializers import ForumSerializer, ForumProjectSerializer




class ForumListCreateView(generics.ListAPIView):
    queryset = Forum.objects.all()
    serializer_class = ForumSerializer

class ForumProjectListCreateView(generics.ListAPIView):
    queryset = ForumProject.objects.all()
    serializer_class = ForumProjectSerializer
