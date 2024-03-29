from rest_framework import serializers
from .models import Post,Notification
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import os
from django.conf import settings

class AuthorSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username')
    # role = serializers.CharField(source='user.role')

    class Meta:
        model = CustomUser
        fields = ['id','username', 'role']


class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    image = serializers.ImageField(required=False)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'published_date', 'author', 'image']
        extra_kwargs = {
            'author': {'read_only': True},
            'image': {'required': False}
        }
def create(self, validated_data):

  image_file = self.context['image_file']

  # Save image
  image_filename = save_image_file(image_file)  

  # Create post 
  post = Post.objects.create(
    **validated_data,
    image=image_filename
  )

  return post
def save_image_file(image_file):

  # save logic 
  image_data = image_file.read()  
  # image_file.save(filename)

  return image_data



class NotificationSerializer(serializers.ModelSerializer):
   class Meta:
       model = Notification
       fields = ['id', 'user', 'username', 'type', 'content']

# class NotificationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Notification
#         fields = '__all__'

from rest_framework import serializers
from .models import Post

class SearchSerializer(serializers.ModelSerializer):
   class Meta:
       model = Post
       fields = ['title', 'body', 'published_date', 'author', 'image']
