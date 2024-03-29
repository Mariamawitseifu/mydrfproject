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
       return Response({'message': 'Post deleted successfully'}, status=status.HTTP_200_OK)
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


from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.status import HTTP_401_UNAUTHORIZED
from news.models import Post
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED
from django.views.decorators.csrf import csrf_exempt
from .serializers import PostSerializer

@api_view(['POST'])
@renderer_classes((JSONRenderer,))
@csrf_exempt
def create_notification(request):
    if request.user.is_authenticated:
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            url = serializer.data.get('url')
            data = {'url': url}
            return Response(data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    else:
        return Response('User must be authenticated to create a post', status=HTTP_401_UNAUTHORIZED)

@csrf_exempt
def mark_notification(request, notification_id):
    if request.method == 'POST':
        try:
            # Get the notification using the notification_id
            notification = Notification.objects.get(id=notification_id)

            # Mark the notification as read
            notification.read = True
            notification.save()

            # Delete the notification
            notification.delete()

            # Assuming you have some data to return in the JSON response
            data = {
                'message': 'Notification marked as read and deleted'
            }

            return JsonResponse(data)
        except Notification.DoesNotExist:
            return JsonResponse({'message': 'Notification not found'}, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse({'message': 'POST request required'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def delete_all_notifications(request):
   if request.method == 'POST':
       Notification.objects.all().delete()
       return JsonResponse({'message': 'All notifications deleted successfully'}, status=200)
   else:
       return JsonResponse({'error': 'POST request required'}, status=400)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def delete_notification(request, notification_id):
   if request.method == 'POST':
       try:
           notification = Notification.objects.get(id=notification_id)
           notification.delete()
           return JsonResponse({'message': 'Notification deleted successfully'}, status=200)
       except Notification.DoesNotExist: 
           return JsonResponse({'error': 'Notification not found'}, status=404)
   else:
       return JsonResponse({'error': 'POST request required'}, status=400)

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

import re
from django.http import JsonResponse
from django.db.models import Q
from .models import Post
from accounts.models import Record

def search_api(request):
    query = request.GET.get('query')  # Assuming search query is passed as a query parameter

    if query:
        # Perform the search using OR condition on multiple fields for both models
        post_results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(body__icontains=query) |
            Q(author__username__icontains=query)
        )

        record_results = Record.objects.filter(
            Q(name__icontains=query) |
            Q(internal_links__icontains=query) |
            Q(external_links__icontains=query)
        )

        # Find the index of the search term in the title and body for posts
        for result in post_results:
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

        # Format the results as dictionaries
        post_results = list(post_results.values())
        record_results = list(record_results.values())
    else:
        # Return all records if no search query is provided
        post_results = list(Post.objects.values())
        record_results = list(Record.objects.values())

    return JsonResponse({'post_results': post_results, 'record_results': record_results})

# from accounts.serializers import RecordSerializer
# from news.serializers import PostSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def combined_detail(request, record_pk, post_pk):
#  try:
#   record = Record.objects.get(pk=record_pk)
#   post = Post.objects.get(pk=post_pk)
#  except (Record.DoesNotExist, Post.DoesNotExist):
#   return JsonResponse({'error': 'Record or Post not found'}, status=404)

#  if request.method == 'GET':
#   record_serializer = RecordSerializer(record)
#   post_serializer = PostSerializer(post)
#   record_data = {
#       'record_id': str(record.id),
#       'name': record_serializer.data.get('name'),
#       'internal_links': record_serializer.data.get('internal_links'),
#       'external_links': record_serializer.data.get('external_links'),
#   }
#   post_data = {
#       'post_id': str(post.id),
#       'title': post_serializer.data.get('title'),
#       'description': post_serializer.data.get('description'),
#   }
#   return JsonResponse({'record': record_data, 'post': post_data})

# from accounts.serializers import RecordSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from news.serializers import PostSerializer

# @csrf_exempt
# def combined_list(request):
#  if request.method == 'GET':
#     records = Record.objects.all()
#     posts = Post.objects.all()
#     record_serializer = RecordSerializer(records, many=True)
#     post_serializer = PostSerializer(posts, many=True)
#     data = []
#     for record, post in zip(record_serializer.data, post_serializer.data):
#         data.append({
#             'record_id': str(record['id']),
#             'name': record['name'],
#             'internal_links': record['internal_links'],
#             'external_links': record['external_links'],
#             'post_id': str(post['id']),
#             'title': post['title'],
#             'description': post.get('description'),
#         })
#     return JsonResponse(data, safe=False)
#  # Add other request methods as needed
