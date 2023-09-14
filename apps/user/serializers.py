from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models
from apps.forum.models import Forum
from rest_framework.pagination import PageNumberPagination
from .utils import send_email, get_uid


class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationSerializer(ModelSerializer):
    class Meta:
        model = models.Inivitation
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    forum_type = serializers.CharField()
    invitation_title = serializers.CharField(
        source="invitation_id.code", read_only=True
    )

    def create(self, validated_data):
        lang = validated_data["access_id"]
        validated_data["access_id"] = ""
        invitation_id = models.Inivitation.objects.filter(
            code=validated_data["invitation_id"]
        ).first()
        if invitation_id and invitation_id.active:
            keys = ""
            trash = validated_data["forum_type"]
            data = trash.split(",")
            data = set(data)
            for f in data:
                if f == ",":
                    continue
                forum = Forum.objects.filter(id=int(f)).first()
                keys += forum.short_key + "-"

            keys = sorted(keys.split("-"))
            keys = list(filter(None, keys))
            keys = "-".join(keys)
            validated_data["access_id"] = keys + "-" + str(get_uid())
            send_email(
                email=validated_data["email"],
                first_name=validated_data["first_name"],
                last_name=validated_data["last_name"],
                access_id=validated_data["access_id"],
                lang=lang,
            )
            validated_data["forum_type"] = list(data)
            user = super().create(validated_data)
            invitation_id.amount -= 1
            if invitation_id.amount<=0:
                invitation_id.active = False
            invitation_id.save()
            return user
        else:
            raise serializers.ValidationError(
                {"error": "User with this access id already exists."}
            )

    class Meta:
        model = models.User
        fields = "__all__"
