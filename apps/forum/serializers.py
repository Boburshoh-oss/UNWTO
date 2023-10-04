from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = models.Organization
        fields = "__all__"

class ForumdetailSerializer(ModelSerializer):
    class Meta:
        model = models.Forum
        fields = "__all__"

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Forum
        fields = ("id", "created", "modified")


class ForumProjectSerializer(ModelSerializer):
    forum_title_uz = serializers.CharField(source="forum.title_uz", read_only=True)
    forum_title_ru = serializers.CharField(source="forum.title_ru", read_only=True)
    forum_title_en = serializers.CharField(source="forum.title_en", read_only=True)
    forum_id = serializers.IntegerField(source="forum.id", read_only=True)

    class Meta:
        model = models.ForumProject
        fields = "__all__"

class EventSerializer(ModelSerializer):
    forum_title = serializers.CharField(source="forum.title", read_only=True)
    forum_id = serializers.IntegerField(source="forum.id", read_only=True)

    class Meta:
        model = models.Event
        fields = ("id", "forum_title", "forum_id", "day", "date", "created", "modified")


class EventTimeSerializer(ModelSerializer):
    event_day = serializers.CharField(source="event.day", read_only=True)

    class Meta:
        model = models.EventTime
        fields = "__all__"


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Map
        fields = ("id", "title","file","created", "modified")