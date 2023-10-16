from django.contrib import admin
from .models import CustomUser, BlogPost

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined')

admin.site.register(CustomUser, CustomUserAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_created', 'date_modified')
    search_fields = ('title', 'author__username')
    list_filter = ('author', 'date_created', 'date_modified')
    readonly_fields = ('date_created', 'date_modified')

admin.site.register(BlogPost, PostAdmin)
