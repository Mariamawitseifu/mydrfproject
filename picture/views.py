from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Picture
from .serializers import PictureSerializer
from rest_framework.decorators import parser_classes
from django.shortcuts import get_object_or_404


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_view(request):
  serializer = PictureSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_view(request, pk):
  picture = get_object_or_404(Picture, pk=pk)
  serializer = PictureSerializer(picture, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_view(request, pk):
  picture = get_object_or_404(Picture, pk=pk)
  picture.delete()
  return Response({'message': 'Picture deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_image(request, pk):
   picture = get_object_or_404(Picture, pk=pk)
   return FileResponse(picture.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_images(request):
  pictures = Picture.objects.all()
  pictures_list = list(pictures.values())
  return Response(pictures_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_view(request):
 Picture.objects.all().delete()
 return Response({'message': 'All pictures deleted successfully'}, status=status.HTTP_200_OK)
