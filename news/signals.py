from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import Notification
from .models import Post

@receiver(post_save, sender=Post)
def create_notification(sender, instance, created, **kwargs):
   if created:
       Notification.objects.create(
           recipient=instance.author,
           text=f'A new blog post "{instance.title}" has been created.'
       )
