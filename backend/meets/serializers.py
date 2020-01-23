from rest_framework import serializers
from .models import Comment, Meet, Profile


class MeetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Meet


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Profile
