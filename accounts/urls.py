# accounts/urls.py

from django.urls import path, include
from .views import register_user, user_login, user_logout
from .views import change_password
from .views import create_blog_post
from .views import create_or_update_blog_post
from .views import update_blog_post,get_single_picture,a_blog_post_added,record_detail,record_list,record_create,delete_record,update_record,record_search_api

urlpatterns = [
    path('a_blog_post_added/', a_blog_post_added, name='get_single_picture'),
    path('singleblog/<int:pk>/', get_single_picture, name='get_single_picture'),
    path('blog/<int:pk>/', update_blog_post, name='update_blog_post'),
    # path('blog-posts-getall' , name='') 
    # path('blog/', create_or_update_blog_post, name='create_or_update_blog_post'),
    path('blog/create/', create_blog_post, name='create_blog_post'),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('change_password/', change_password, name='change_password'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/records/', record_list, name='record-list'),
    path('api/records/<int:pk>/', record_detail, name='record-detail'),
    path('api/records/create/', record_create, name='record-create'),
    path('api/records/delete/<int:pk>/',delete_record, name='delete_record'),
    path('records/<int:pk>/', update_record, name='update_record'),
    path('api/record/search/', record_search_api, name='record_search_api'),
]