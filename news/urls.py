from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


from .views import post_list,post_detail,create_post,delete_post,delete_all_posts,notification_list
urlpatterns = [
    # Other URL patterns
    path('api1/', include('rest_framework.urls')),
    path('posts/', post_list, name='post-list'),
    path('posts/<slug:slug>/', post_detail, name='post-detail'),
    path('createpost/',create_post,name='create_post'),
    path('deleteposts/<int:id>/', delete_post, name='delete_post'),
    path('deleteposts/delete-all/', delete_all_posts, name='delete_all_posts'),
    path('notifications/', notification_list),
    # path('notifications/', notification_list_view, name='notification-list'),
    # path('notifications/mark-as-read/<int:pk>/', mark_notification_as_read_view, name='mark-notification-as-read'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)