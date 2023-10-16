from django.shortcuts import render

# from django.http import JsonResponse
# from haystack.query import SearchQuerySet
# Create your views here.
# accounts/views.py

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import BlogPost
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogPostSerializer,BlogPostUserSerializer
# from api.auth.permissions import IsAdminUser
from rest_framework import status
from .models import CustomUser


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# accounts/views.py

from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser

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
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
    # accounts/views.py



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# accounts/views.py



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
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "danikasparov@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
    
class PostViewset(ModelViewSet):
    serializer_class = BlogPostSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get_queryset(self):
        return Post.objects.all()
    

class GetPostsAPIView(APIView):
    serializer_class = BlogPostSerializer
    # permission_classes = [IsAuthenticated]
    # queryset = User.objects.all()
    def get(self, request):
        posts=BlogPost.objects.all()
        return(BlogPostSerializer(posts).data)
    
    
class PostUserAPIView(APIView):
    # serializer_class = [PostUserSerializer]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request):
        posts = BlogPost.objects.all()
        return Response({"msg": BlogPostSerializer(posts).data})
        
# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
# def create_blog_post(request):
#     if request.method == 'POST':
#         # Retrieve the necessary data from the request
#         title = request.POST.get('title')
#         body = request.POST.get('body')
        
#         # Perform any necessary validation or data processing
        
#         # Save the blog post to the database or perform other actions
        
#         # Return a JSON response with a success message or relevant data
#         return JsonResponse({'message': 'Blog post created successfully'})
    
#     # Return an error response if the request method is not POST
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework import serializers

# class BlogPostSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     body = serializers.CharField()

# @csrf_exempt
# def create_blog_post(request):
#     if request.method == 'POST':
#         serializer = BlogPostSerializer(data=request.POST)
        
#         if serializer.is_valid():
#             # Retrieve the validated data from the serializer
#             title = serializer.validated_data['title']
#             body = serializer.validated_data['body']
            
#             # Perform any necessary validation or data processing
            
#             # Save the blog post to the database or perform other actions
            
#             # Return a JSON response with the created blog post data
#             return JsonResponse({'title': title, 'body': body})
        
#         # Return a JSON response with the validation errors if the serializer is not valid
#         return JsonResponse(serializer.errors, status=400)
    
#     # Return an error response if the request method is not POST
#     return JsonResponse({'error': 'Invalid request method'}, status=405)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_blog_post(request):
    if request.method == 'POST':
        serializer = BlogPostSerializer(data=request.data)
        
        if serializer.is_valid():
            # Retrieve the validated data from the serializer
            title = serializer.validated_data['title']
            body = serializer.validated_data['body']
            
            # Perform any necessary validation or data processing
            
            # Save the blog post to the database or perform other actions
            
            # Return a JSON response with the created blog post data
            return Response({'title': title, 'body': body}, status=status.HTTP_201_CREATED)
        
        # Return a JSON response with the validation errors if the serializer is not valid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Return an error response if the request method is not POST
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)





# from django.http import JsonResponse
# from django.contrib.postgres.search import SearchVector
# from .models import BlogPost

# def search_view(request):
#     query = request.GET.get('query')

#     if query:
#         # Perform search on both Page and Article models
#         page_results = BlogPost.objects.annotate(search=SearchVector('title', 'body')).filter(search=query)
#         # article_results = Article.objects.annotate(search=SearchVector('title', 'body')).filter(search=query)

#         # Prepare the search results as a list of dictionaries
#         results = []
#         for page in page_results:
#             results.append({'type': 'BlogPost', 'title': page.title, 'body': page.body})
#     #     for article in article_results:
#     #         results.append({'type': 'Article', 'title': article.title, 'body': article.body})
#     # else:
#         results = []

#     return JsonResponse({'results': results})