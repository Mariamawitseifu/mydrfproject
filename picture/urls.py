from django.urls import path
# from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import create_view, update_view, delete_view,serve_image,fetch_all_images,delete_all_view

urlpatterns = [
  path('create/', create_view, name='create'),
  path('update/<int:pk>/', update_view, name='update'),
  path('delete/<int:pk>/', delete_view, name='delete'),
  path('delete/', delete_all_view, name='delete_all'),
  path('image/<int:pk>/', serve_image, name='serve_image'),
  path('images/', fetch_all_images, name='fetch_all_images'),
  
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
