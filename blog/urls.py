from django.urls import path
from django.urls import include

from .views import post_list,post_detail,create_post,delete_post,delete_all_posts
urlpatterns = [
    # Other URL patterns
    path('api1/', include('rest_framework.urls')),
    path('posts/', post_list, name='post-list'),
    path('posts/<slug:slug>/', post_detail, name='post-detail'),
    path('createpost/',create_post,name='create_post'),
    path('deleteposts/<int:id>/', delete_post, name='delete_post'),
    path('deleteposts/delete-all/', delete_all_posts, name='delete_all_posts'),
]
