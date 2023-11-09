from accounts.models import CustomUser
from datetime import datetime
from django.dispatch import Signal
from news.models import Notification
from news.serializers import NotificationSerializer
from PIL import Image
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers
from .serializers import PostSerializer
from .models import Post
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.decorators import parser_classes


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_post(request):
    # image_file = request.FILES.get('image')
    serializer = PostSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        print(request.user)
        serializer.save(author=CustomUser.objects.get(username=request.user.username))
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_all_posts(request):
    Post.objects.all().delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def notification_list_view(request):
    user = request.user
    notifications = Notification.objects.filter(recipient=user).order_by('-created_at')
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def mark_notification_as_read_view(request, pk):
    try:
        notification = Notification.objects.get(pk=pk)
        notification.read = True
        notification.save()
        return Response({'message': 'Notification marked as read.'})
    except Notification.DoesNotExist:
        return Response({'error': 'Notification does not exist.'}, status=status.HTTP_404_NOT_FOUND)