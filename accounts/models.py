from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    admin = 'admin'
    superadmin = 'superadmin'
    MANAGER = 'manager'
    USER = 'user'

    ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('superadmin', 'Superadmin'),
    (MANAGER, 'Manager'),
    (USER, 'User'),
    )
    
    name = models.CharField(blank=True, max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(choices=ROLE_CHOICES,max_length=20, blank=True, null=True, default=USER)
    # Add custom fields here, if needed

    def __str__(self):
        return self.username



class Record(models.Model):
    order = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    internal_links = models.CharField(max_length=255, blank=True, null=True)
    external_links = models.CharField(max_length=255,  blank=True, null=True)

    def __str__(self):
        return f"{self.order}: {self.name}"
    



