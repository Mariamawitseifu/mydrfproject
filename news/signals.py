from django.db.models.signals import post_save
from django.dispatch import receiver
from news.models import Notification
from .models import Post

@receiver(post_save, sender=Post)
def create_notification(sender, instance, created, **kwargs):
   if created:
        post = Post.objects.get(id=instance.id) # Get the Post object
        post.refresh_from_db() # Refresh the Post object
        Notification.objects.create(
        post_id=post.id,
           recipient=instance.author,
           text=f'"{instance.author.username}" posted a new blog.'

       )
