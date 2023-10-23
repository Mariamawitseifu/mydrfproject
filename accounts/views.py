from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, BlogPostSerializer, ChangePasswordSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash, authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework.decorators import api_view
from .models import BlogPost

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            response_data = {
                'user': serializer.data,
                'token': token.key
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset for {title}".format(title="Some website title"),
        email_plaintext_message,
        "danikasparov@somehost.local",
        [reset_password_token.user.email]
    )

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_blog_post(request):
    if request.method == 'GET':
        blog_post = BlogPost.objects.get(id=request.GET.get('id'))
        serializer = BlogPostSerializer(blog_post)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def create_or_update_blog_post(request):
    if request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    blog_post = get_object_or_404(BlogPost, pk=request.data.get('id'))
    serializer = BlogPostSerializer(blog_post, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_blog_post(request, pk):
    try:
        blog_post = BlogPost.objects.get(pk=pk, user=request.user)
    except BlogPost.DoesNotExist:
        return Response({'error': 'Blog post not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BlogPostSerializer(blog_post, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_picture(request,id):
    serializer = BlogPost.objects.get(id=request.GET.get('id'))
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
   
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def a_blog_post_added(request):
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Record
from .serializers import RecordSerializer
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def record_list(request):
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def record_detail(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        record.delete()
        return JsonResponse({'message': 'Record deleted successfully'}, status=204)
    
from django.http import JsonResponse

@csrf_exempt
def record_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)