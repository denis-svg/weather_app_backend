from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password" : {"write_only":True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
    read_only=True,
    slug_field="username"
  )
    class Meta:
        model = Comment
        fields = ["id", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only":True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]