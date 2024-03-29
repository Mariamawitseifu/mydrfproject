from django.db import models

class Picture(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_gallery'
      
class PictureDroga(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_droga'

class PictureEma(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_ema'
      
class PictureTrust(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_trust'
    
class PicturePhysio(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_Physio'
      
class PictureRwanda(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_rwanda'
      
class PictureSom(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_som'
      
class PictureChain(models.Model):
   image = models.ImageField(upload_to='blog_images/', null=False, blank=False)
   title = models.CharField(max_length=255)
   def __str__(self):
       if self.image:
           return str(self.image)
       else:
           return "No Image"
   class Meta:
      db_table = 'picture_chain'