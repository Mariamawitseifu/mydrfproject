from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Picture,PictureDroga,PictureEma,PictureChain,PictureTrust,PictureSom,PictureRwanda,PicturePhysio
from .serializers import PictureSerializer,PictureDrogaSerializer,PictureEmaSerializer,PictureTrustSerializer,PictureChainSerializer,PicturePhysioSerializer,PictureSomSerializer,PictureRwandaSerializer
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



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewd(request):
  serializer = PictureDrogaSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewd(request, pk):
  PictureDroga = get_object_or_404(PictureDroga, pk=pk)
  serializer = PictureDrogaSerializer(PictureDroga, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewd(request, pk):
  pictureDroga = get_object_or_404(PictureDroga, pk=pk)
  pictureDroga.delete()
  return Response({'message': 'PictureDroga deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imaged(request, pk):
   PictureDroga = get_object_or_404(PictureDroga, pk=pk)
   return FileResponse(PictureDroga.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagesd(request):
  PictureDrogas = PictureDroga.objects.all()
  PictureDrogas_list = list(PictureDrogas.values())
  return Response(PictureDrogas_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewd(request):
 PictureDroga.objects.all().delete()
 return Response({'message': 'All PictureDrogas deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewe(request):
  serializer = PictureEmaSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewe(request, pk):
  PictureEma = get_object_or_404(PictureEma, pk=pk)
  serializer = PictureEmaSerializer(PictureEma, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewe(request, pk):
  pictureEma = get_object_or_404(PictureEma, pk=pk)
  pictureEma.delete()
  return Response({'message': 'PictureEma deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imagee(request, pk):
   PictureEma = get_object_or_404(PictureEma, pk=pk)
   return FileResponse(PictureEma.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagese(request):
  PictureEmas = PictureEma.objects.all()
  PictureEmas_list = list(PictureEmas.values())
  return Response(PictureEmas_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewe(request):
 PictureEma.objects.all().delete()
 return Response({'message': 'All PictureEmas deleted successfully'}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewt(request):
  serializer = PictureTrustSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewt(request, pk):
  PictureTrust = get_object_or_404(PictureTrust, pk=pk)
  serializer = PictureTrustSerializer(PictureTrust, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewt(request, pk):
  pictureTrust = get_object_or_404(PictureTrust, pk=pk)
  pictureTrust.delete()
  return Response({'message': 'PictureTrust deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imaget(request, pk):
   PictureTrust = get_object_or_404(PictureTrust, pk=pk)
   return FileResponse(PictureTrust.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagest(request):
  PictureTrusts = PictureTrust.objects.all()
  PictureTrusts_list = list(PictureTrusts.values())
  return Response(PictureTrusts_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewt(request):
 PictureTrust.objects.all().delete()
 return Response({'message': 'All PictureTrusts deleted successfully'}, status=status.HTTP_200_OK)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewc(request):
  serializer = PictureChainSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewc(request, pk):
  PictureChain = get_object_or_404(PictureChain, pk=pk)
  serializer = PictureChainSerializer(PictureChain, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewc(request, pk):
 picture_chain = get_object_or_404(PictureChain, pk=pk)
 picture_chain.delete()
 return Response({'message': 'PictureChain deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imagec(request, pk):
   PictureChain = get_object_or_404(PictureChain, pk=pk)
   return FileResponse(PictureChain.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagesc(request):
  PictureChains = PictureChain.objects.all()
  PictureChains_list = list(PictureChains.values())
  return Response(PictureChains_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewc(request):
 PictureChain.objects.all().delete()
 return Response({'message': 'All PictureChains deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewp(request):
  serializer = PicturePhysioSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewp(request, pk):
  PicturePhysio = get_object_or_404(PicturePhysio, pk=pk)
  serializer = PicturePhysioSerializer(PicturePhysio, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewp(request, pk):
  picturePhysio = get_object_or_404(PictureChain, pk=pk)
  picturePhysio.delete()
  return Response({'message': 'PicturePhysio deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imagep(request, pk):
   PicturePhysio = get_object_or_404(PicturePhysio, pk=pk)
   return FileResponse(PicturePhysio.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagesp(request):
  PicturePhysios = PictureChain.objects.all()
  PicturePhysios_list = list(PicturePhysios.values())
  return Response(PicturePhysios_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewp(request):
 PicturePhysio.objects.all().delete()
 return Response({'message': 'All PicturePhysios deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_views(request):
  serializer = PictureSomSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_views(request, pk):
  PictureSom = get_object_or_404(PictureSom, pk=pk)
  serializer = PictureSomSerializer(PictureSom, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_views(request, pk):
  pictureSom = get_object_or_404(PictureSom, pk=pk)
  pictureSom.delete()
  return Response({'message': 'PictureSom deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_images(request, pk):
   PictureSom = get_object_or_404(PictureSom, pk=pk)
   return FileResponse(PictureSom.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagess(request):
  PictureSoms = PictureSom.objects.all()
  PictureSoms_list = list(PictureSoms.values())
  return Response(PictureSoms_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_views(request):
 PictureSom.objects.all().delete()
 return Response({'message': 'All PictureSoms deleted successfully'}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_viewr(request):
  serializer = PictureRwandaSerializer(data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def update_viewr(request, pk):
  PictureRwanda = get_object_or_404(PictureRwanda, pk=pk)
  serializer = PictureRwandaSerializer(PictureRwanda, data=request.data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_viewr(request, pk):
  pictureRwanda = get_object_or_404(PictureRwanda, pk=pk)
  pictureRwanda.delete()
  return Response({'message': 'PictureRwanda deleted successfully'}, status=status.HTTP_200_OK)

from django.http import FileResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def serve_imager(request, pk):
   PictureRwanda = get_object_or_404(PictureRwanda, pk=pk)
   return FileResponse(PictureRwanda.image.open(), content_type='image/jpeg')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def fetch_all_imagesr(request):
  PictureRwandas = PictureRwanda.objects.all()
  PictureRwandas_list = list(PictureRwandas.values())
  return Response(PictureRwandas_list, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_all_viewr(request):
 PictureRwanda.objects.all().delete()
 return Response({'message': 'All PictureRwandas deleted successfully'}, status=status.HTTP_200_OK)
