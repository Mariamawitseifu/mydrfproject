from django.urls import path
# from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from .views import create_view, update_view, delete_view,serve_image,fetch_all_images,delete_all_view,create_viewd, update_viewd, delete_viewd,serve_imaged,fetch_all_imagesd,delete_all_viewd,create_viewe, update_viewe, delete_viewe,serve_imagee,fetch_all_imagese,delete_all_viewe,delete_all_viewt,create_viewt,fetch_all_imagest, update_viewt, delete_viewt,serve_imaget,fetch_all_imagesc,delete_all_viewc,create_viewc, update_viewc, delete_viewc,serve_imagec,fetch_all_imagesc,delete_all_viewc,create_viewp, update_viewp, delete_viewp,serve_imagep,fetch_all_imagesp,delete_all_viewp,create_views, update_views, delete_views,serve_images,fetch_all_imagess,delete_all_views,create_viewr, update_viewr, delete_viewr,serve_imager,fetch_all_imagesr,delete_all_viewr

urlpatterns = [
  path('create/', create_view, name='create'),
  path('update/<int:pk>/', update_view, name='update'),
  path('delete/<int:pk>/', delete_view, name='delete'),
  path('delete/', delete_all_view, name='delete_all'),
  path('image/<int:pk>/', serve_image, name='serve_image'),
  path('images/', fetch_all_images, name='fetch_all_images'),
  
  path('created/', create_viewd, name='create'),
  path('updated/<int:pk>/', update_viewd, name='update'),
  path('deleted/<int:pk>/', delete_viewd, name='delete'),
  path('deleted/', delete_all_viewd, name='delete_all'),
  path('imaged/<int:pk>/', serve_imaged, name='serve_image'),
  path('imagesd/', fetch_all_imagesd, name='fetch_all_images'),
  
  path('createe/', create_viewe, name='create'),
  path('updatee/<int:pk>/', update_viewe, name='update'),
  path('deletee/<int:pk>/', delete_viewe, name='delete'),
  path('deletee/', delete_all_viewe, name='delete_all'),
  path('imagee/<int:pk>/', serve_imagee, name='serve_image'),
  path('imagese/', fetch_all_imagese, name='fetch_all_images'),
  
  path('createt/', create_viewt, name='create'),
  path('updatet/<int:pk>/', update_viewt, name='update'),
  path('deletet/<int:pk>/', delete_viewt, name='delete'),
  path('deletet/', delete_all_viewt, name='delete_all'),
  path('imaget/<int:pk>/', serve_imaget, name='serve_image'),
  path('imagest/', fetch_all_imagest, name='fetch_all_images'),
  
  path('createc/', create_viewc, name='create'),
  path('updatec/<int:pk>/', update_viewc, name='update'),
  path('deletec/<int:pk>/', delete_viewc, name='delete'),
  path('deletec/', delete_all_viewc, name='delete_all'),
  path('imagec/<int:pk>/', serve_imagec, name='serve_image'),
  path('imagesc/', fetch_all_imagesc, name='fetch_all_images'),
  
  path('createp/', create_viewp, name='create'),
  path('updatep/<int:pk>/', update_viewp, name='update'),
  path('deletep/<int:pk>/', delete_viewp, name='delete'),
  path('deletep/', delete_all_viewp, name='delete_all'),
  path('imagep/<int:pk>/', serve_imagep, name='serve_image'),
  path('imagesp/', fetch_all_imagesp, name='fetch_all_images'),
  
  path('creates/', create_views, name='create'),
  path('updates/<int:pk>/', update_views, name='update'),
  path('deletes/<int:pk>/', delete_views, name='delete'),
  path('deletes/', delete_all_views, name='delete_all'),
  path('images/<int:pk>/', serve_images, name='serve_image'),
  path('imagess/', fetch_all_imagess, name='fetch_all_images'),
  
  path('creater/', create_viewr, name='create'),
  path('updater/<int:pk>/', update_viewr, name='update'),
  path('deleter/<int:pk>/', delete_viewr, name='delete'),
  path('deleter/', delete_all_viewr, name='delete_all'),
  path('imager/<int:pk>/', serve_imager, name='serve_image'),
  path('imagesr/', fetch_all_imagesr, name='fetch_all_images'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
