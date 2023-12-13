from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static


from .views import post_list,post_detail,create_post,delete_post,delete_all_posts,notification_list,create_notification,notification_list,mark_notification,delete_notification,delete_all_notifications,search_api

urlpatterns = [
    # Other URL patterns
    path('api1/', include('rest_framework.urls')),
    path('posts/', post_list, name='post-list'),
    # path('posts/<slug:slug>/', post_detail, name='post-detail'),
    path('createpost/',create_post,name='create_post'),
    path('deleteposts/<int:id>/', delete_post, name='delete_post'),
    path('deleteposts/delete-all/', delete_all_posts, name='delete_all_posts'),
    # path('notifications/', notification_list),
    path('notifications/', notification_list, name='notification-list'),
    path('notifications/mark-as-read/<int:notification_id>/', mark_notification, name='mark-notification-as-read'),
    path('notifications/create/', create_notification, name='create-notification'),
    # path('api/search/', post_search_api, name='post_search_api'),
    path('posts/<int:id>/', post_detail, name='post-detail'),
    path('delete_notification/<int:notification_id>/', delete_notification, name='delete_notification'),
    path('delete_all_notifications/', delete_all_notifications),
    # path('api/combined_search/', combined_search_api, name='combined_search_api'),
    path('search/',search_api, name='search_api'),
    # path('api/details/<uuid:record_pk>/<uuid:post_pk>/',combined_detail),
    # path('api/details/',combined_list),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)