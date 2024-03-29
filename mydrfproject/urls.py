# # mydrfproject/urls.py

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('accounts.urls')),  # Include the app's URLs
# ]
from django.conf import settings
from django.conf.urls.static import static
# mydrfproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),  # Include the app's URLs
    path('api1/', include('news.urls')),
    path('pictures/', include('picture.urls')),
    path('myapp', include("django_nextjs.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)