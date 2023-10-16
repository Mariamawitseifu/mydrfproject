# accounts/urls.py

from django.urls import path, include
from .views import register_user, user_login, user_logout
from .views import change_password
from .views import PostUserAPIView
from .views import create_blog_post
# from .views import search_view

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('api/posts', GetPostsAPIView.as_view(), name='get_posts'),
    path('api/postuser', PostUserAPIView.as_view(), name='post_user'),
    path('api/blog/', create_blog_post, name='create_blog_post'),
    # path('search/', search_view, name='search'),
]
# http://127.0.0.1:8000/api/register/

# urls.py
