from django.db import models
from django.db.models import (Model, CharField, IntegerField,
                            DateField, DecimalField,
                            DateTimeField, ForeignKey, EmailField,
                            TextField, BooleanField, URLField, CASCADE, SET_NULL,UUIDField, OneToOneField, ManyToManyField
                            )
from django.contrib.postgres.search import SearchVectorField
from django.contrib.postgres.indexes import GinIndex    
# from autoslug import AutoSlugField

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add custom fields here, if needed

    def __str__(self):
        return self.username
    
    
class BlogPost(Model):
    title = CharField(max_length=255, unique=True)
    # sub_title = CharField(max_length=255, blank=True, null=True)
    # slug = AutoSlugField(populate_from='title', unique=True, unique_with=['date_created'])
    slug = models.SlugField(max_length=255)
    body = TextField()
    meta_description = CharField(max_length=150, blank=True, null=True)
    date_created = DateTimeField(auto_now_add=True)
    date_modified = DateTimeField(auto_now=True)
    # publish_date = DateTimeField(blank=True, null=True)
    # published = BooleanField(default=True)
    author = ForeignKey(CustomUser, related_name="posts", on_delete=CASCADE)
    # tags = ManyToManyField(Tag, blank=True)
    search_vector = SearchVectorField(null=True)  # Field for search indexing

    class Meta:
        indexes = [GinIndex(fields=['search_vector'])]  # Index for search vector
    class Meta:
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'
    
    def comments(self):
        if not hasattr(self, '_comments'):
            self._comments = self.comments
        return self._comments