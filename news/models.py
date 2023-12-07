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
    blank=True,
)
    # slug = models.SlugField(max_length=200, unique=True) # Add this line

    
    def __str__(self):
        return self.author.username
    
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    # slug = models.SlugField(unique=True)
    def __str__(self):
        if self.image:
            return str(self.image)
        else:
            return "No Image"
        
    def get_absolute_url(self):
        return f'/posts/{self.id}'   
# from django.db import models
# from django.contrib.auth.models import User

# class Notification(models.Model):
#    USER_TYPE = (
#        ('blog', 'Blog'),
#        ('quick_link', 'Quick Link'),
#        ('picture', 'Picture'),
#    )
#    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
#    username = models.CharField(max_length=200)
#    type = models.CharField(max_length=20, choices=USER_TYPE)
#    content = models.TextField()
from django.contrib.auth import get_user_model
from accounts.models import CustomUser
class Notification(models.Model):
    # user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.user.username