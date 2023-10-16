# accounts/serializers.py

from rest_framework import serializers
from .models import CustomUser
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import BlogPost
from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from api.users.serializers import UserSerializer
import json
import contextlib



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
# accounts/serializers.py

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    
    
class BlogPostUserSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'sub_title', 'body', 'date_created', 'date_modified',
           'slug', 'author'
            ]
        
class BlogPostSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    # def create(self, validated_data):
    #     request = self.context['request']
    #     author_id = request.data.get('author')
    #     validated_data['author_id'] = author_id
    #     return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     request = self.context['request']
    #     author_id = request.data.get('author')
    #     validated_data['author_id'] = author_id
    #     return super().update(instance, validated_data)

    class Meta:
        model = BlogPost
        # fields = '__all__'
        fields = ('title', 'body')