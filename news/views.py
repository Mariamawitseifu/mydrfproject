from accounts.models import CustomUser
from datetime import datetime
from django.dispatch import Signal
# from news.models import Notification
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
from .models import Notification
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated, BasePermission

class IsManagerOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.role == 'manager' or request.user.role == 'superadmin')
        )
        
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsManagerOrSuperAdmin])
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

# @api_view(['POST'])
# @permission_classes([IsAuthenticated, IsManager])
# @parser_classes([MultiPartParser, FormParser])
# def create_post(request):
#     # image_file = request.FILES.get('image')
#     serializer = PostSerializer(data=request.data)
#     print(request.data)
#     if serializer.is_valid():
#         print(request.user)
#         serializer.save(author=CustomUser.objects.get(username=request.user.username))
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def post_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, id):
   try:
       post = Post.objects.get(id=id)
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

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

@api_view(['GET', 'POST'])
def notification_list(request):
 if request.method == 'GET':
     notifications = Notification.objects.all()
     serializer = NotificationSerializer(notifications, many=True)
     return Response(serializer.data)

 elif request.method == 'POST':
     serializer = NotificationSerializer(data=request.data)
     if serializer.is_valid():
         serializer.save()
     return Response(serializer.data)
 
import re
from django.db.models import Q
from django.http import JsonResponse
from .models import Post

def post_search_api(request):
   query = request.GET.get('query') # Assuming search query is passed as a query parameter

   if query:
       # Perform the search using OR condition on multiple fields
       results = Post.objects.filter(
           Q(title__icontains=query) |
           Q(body__icontains=query) |
           Q(author__username__icontains=query)
       )
   else:
       results = Post.objects.all() # Return all records if no search query is provided

   # Find the index of the search term in the title and body
   for result in results:
    if query:
       title_index = re.search(query, result.title)
       body_index = re.search(query, result.body)

       # Slice the title and body around the index
       if title_index:
           start = max(0, title_index.start() - 15)
           end = title_index.end() + 15
           result.title = ' '.join(result.title.split()[start:end])

       if body_index:
           start = max(0, body_index.start() - 15)
           end = body_index.end() + 15
           result.body = ' '.join(result.body.split()[start:end])

   return JsonResponse({'results': list(results.values())})
