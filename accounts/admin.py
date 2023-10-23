from django.contrib import admin
from .models import CustomUser
from .models import BlogPost
from .models import Record  

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
admin.site.register(Record)
admin.site.unregister(BlogPost)
