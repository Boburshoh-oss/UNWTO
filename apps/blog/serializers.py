from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models


class BannerSerializer(ModelSerializer):
    class Meta:
        model = models.Banner
        fields = "__all__"


class ContactSerializer(ModelSerializer):
    class Meta:
        model = models.Connect
        fields = "__all__"

