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
        fields = ("id", "created", "modified", "title", "description")


class ForumProjectSerializer(ModelSerializer):
    forum_title = serializers.CharField(source="forum.title", read_only=True)
    forum_id = serializers.IntegerField(source="forum.id", read_only=True)

    class Meta:
        model = models.ForumProject
        fields = ("id", "forum_title", "forum_id", "title", "subtitle", "image", "context", "created", "modified")


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
