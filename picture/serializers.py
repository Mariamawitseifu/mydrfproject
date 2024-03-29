from rest_framework import serializers
from .models import Picture,PictureDroga,PictureEma,PictureChain,PictureTrust,PictureSom,PictureRwanda,PicturePhysio

class PictureSerializer(serializers.ModelSerializer):
   class Meta:
       model = Picture
       fields = ['id', 'image','title']

class PictureDrogaSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureDroga
       fields = ['id', 'image','title']
class PictureEmaSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureEma
       fields = ['id', 'image','title']
class PictureTrustSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureTrust
       fields = ['id', 'image','title']

class PictureSomSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureSom
       fields = ['id', 'image','title']

class PictureChainSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureChain
       fields = ['id', 'image','title']

class PictureRwandaSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureRwanda
       fields = ['id', 'image','title']

class PicturePhysioSerializer(serializers.ModelSerializer):
   class Meta:
       model = PictureChain
       fields = ['id', 'image','title']
