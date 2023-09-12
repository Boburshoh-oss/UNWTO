from django.db.models import F, ExpressionWrapper
from rest_framework.pagination import PageNumberPagination
from apps.forum.utils.list_api_view import MyListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from . import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# from translation import ForumTranslationOptions
class PaginationReport(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = "page_size"
    max_page_size = 100


# Organizations Apis
class OrganizationApiView(MyListAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer
    pagination_class = PaginationReport
    
class OrganizationDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer


# Forum Apis
class ForumApiView(APIView):
    pagination_class = PaginationReport

    def get(self, request):
        queryset = models.Forum.objects.all().order_by('-pk')
        queryset = queryset.annotate(
            forum_title=F('title')
        )

        # Instantiate the paginator
        paginator = self.pagination_class()

        # Paginate the queryset
        result_page = paginator.paginate_queryset(queryset, request)

        # Serialize the paginated data
        serializer = serializers.ForumSerializer(result_page, many=True)

        # Return the paginated response with organization titles
        response_data = serializer.data
        for forum_data in response_data:
            forum = models.Forum.objects.get(id=forum_data['id'])
            forum_data['title_uz'] = forum.title_uz
            forum_data['title_ru'] = forum.title_ru
            forum_data['title_en'] = forum.title_en
            forum_data['description_uz'] = forum.description_uz
            forum_data['description_ru'] = forum.description_ru
            forum_data['description_en'] = forum.description_en
            forum_event = models.Event.objects.filter(forum=forum).order_by('ordered')
            forum_data['events'] = []
            for event in forum_event:
                forum_day_times = models.EventTime.objects.filter(event=event).order_by('start_time')
                title = event.day_uz
                times = []
                for event_time in forum_day_times:
                    times.append({
                        'start_time' : event_time.start_time.strftime("%H:%M"),
                        'end_time' : event_time.end_time.strftime("%H:%M"),
                        'description_uz' : event_time.description_uz,
                        'description_ru' : event_time.description_ru,
                        'description_en' : event_time.description_en
                    })
                forum_data['events'].append({'times':times, 
                                             'event_day_uz': event.day_uz,
                                             'event_day_ru': event.day_ru,
                                             'event_day_en': event.day_en,
                                             })
            forum_data['organizations'] = [{'organization_title_uz': organization.title_uz,'organization_title_en': organization.title_en,'organization_title_ru': organization.title_ru, 'organization_id': organization.id} for organization in forum.organization.all()]
        return paginator.get_paginated_response(response_data)


class ForumCreateApiView(CreateAPIView):
    queryset = models.Forum.objects.all()
    serializer_class = serializers.ForumSerializer


class ForumDetailApiView(APIView):
    def get(self, request, pk):
        forum = models.Forum.objects.get(id=pk)
        serializer = serializers.ForumSerializer(forum)
        response_data = serializer.data
        response_data['organizations'] = [{'organization_title': organization.title, 'organization_id': organization.id} for organization in forum.organization.all()]
        return Response(response_data)

    def put(self, request, pk):
        forum = models.Forum.objects.get(id=pk)
        serializer = serializers.ForumdetailSerializer(forum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        forum = models.Forum.objects.get(id=pk)
        forum.delete()
        return Response({"message": "Forum deleted successfully"})

# ForumProject Apis
class ForumProjectListApiView(MyListAPIView):
    queryset = models.ForumProject.objects.all().order_by('-pk')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.annotate(
            forum_title_uz=F('forum__title_uz'),
            forum_title_ru=F('forum__title_ru'),
            forum_title_en=F('forum__title_en')
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
class EventTimeApiView(MyListAPIView):

    def get_queryset(self):
        forum_id = self.request.query_params.get('forum_id', None)
        queryset = models.EventTime.objects.filter(event__forum__id=forum_id)
        queryset = queryset.annotate(
            event_day=F('event__day')
        )
        return queryset
    serializer_class = serializers.EventTimeSerializer
    pagination_class = PaginationReport

class EventTimeDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = models.EventTime.objects.all()
    serializer_class = serializers.EventTimeSerializer


