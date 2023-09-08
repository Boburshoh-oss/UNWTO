from rest_framework import serializers
from .models import Forum, ForumProject




class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class ForumProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumProject
        fields = '__all__'
