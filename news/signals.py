from django.dispatch import receiver
from models import Notification  # Assuming you have a notifications app and Notification model
from accounts.models import CustomUser
from models import new_blog_post_signal

@receiver(new_blog_post_signal)
def create_notification(sender, post, **kwargs):
    recipients = CustomUser.objects.all()  # Change this to select specific recipients if needed
    message = f"A new blog post '{post.title}' has been published."

    for recipient in recipients:
        notification = Notification(recipient=recipient, message=message, post=post)
        notification.save()
