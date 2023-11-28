from django.db import models

class Picture(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_gallery'
