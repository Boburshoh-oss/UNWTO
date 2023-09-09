from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from . import models
from apps.forum.models import Forum
from apps.forum.serializers import ForumSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.response import Response

class MyPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class InivitationSerializer(ModelSerializer):
    class Meta:
        model = models.Inivitation
        fields = "__all__"
    


class UserSerializer(serializers.ModelSerializer):
    forum_type = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Forum.objects.all()
    )

    def create(self, validated_data):
        invitation_id = models.Inivitation.objects.filter(
            code=validated_data['invitation_id']
        ).first()
        print(validated_data)
        if invitation_id and invitation_id.active:
            invitation_id.active=False
            invitation_id.save()
            return super().create(validated_data)
        else:
            return Response(
                {"error": "User with this access id already exists."}, status=status.HTTP_400_BAD_REQUEST
            )
    class Meta:
        model = models.User
        fields = "__all__"
