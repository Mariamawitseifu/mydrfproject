from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    class Meta:
        db_table = 'blog_post'

    title = models.CharField(max_length=255)
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
    'accounts.CustomUser',
    on_delete=models.SET_DEFAULT,
    default=None,
    blank=True
)

    
    def __str__(self):
        return self.author.username
    
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    # slug = models.SlugField(unique=True)
    def __str__(self):
        if self.image:
            return str(self.image)
        else:
            return "No Image"
          
class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    published_date = models.DateTimeField(default=timezone.now)

    # ... other fields and methods ...

    def __str__(self):
        return self.message