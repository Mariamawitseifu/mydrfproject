from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomUserSerializer, ChangePasswordSerializer
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.urls import reverse
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import update_session_auth_hash, authenticate
from django.core.exceptions import ObjectDoesNotExist
from .models import CustomUser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register_user(request):
    # Check if the user making the request is admin or superadmin
    # if request.user.role not in ['admin', 'superadmin']:
    #     return Response({'error': 'Only admin and superadmin can perform this action.'}, status=status.HTTP_403_FORBIDDEN)

    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        # Get the role from the request data
        role = request.data.get('role', '').lower()  # Convert to lowercase

        # Check if the role is valid
        role_choices = dict(CustomUser.ROLE_CHOICES)
        if role not in role_choices:
            return Response({'error': 'Invalid role.'}, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()

        # Assign the role to the user
        user.role = role
        user.save()

        token, _ = Token.objects.get_or_create(user=user)
        response_data = {
            'user': serializer.data,
            'token': token.key,
            'role': user.role
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass

        if not user:
            user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            serializer = CustomUserSerializer(user)
            response_data = {
                'user': serializer.data,
                'token': token.key
            }
            return Response(response_data, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        "Password Reset for {title}".format(title="Some website title"),
        email_plaintext_message,
        "mariamawits@drogapharma.com",
        [reset_password_token.user.email]
    )
    
from rest_framework.permissions import IsAuthenticated, BasePermission

class IsAdminOrSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (request.user.role == 'admin' or request.user.role == 'superadmin')
        )

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login

@api_view(['POST'])
def reset_password_to_default(request, user_id):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Reset the password to "12345"
        user.password = make_password('12345')
        user.save()

        # Update the last login time to invalidate the current session
        update_last_login(None, user)

        return Response({'message': 'Password reset to default successfully.'}, status=status.HTTP_200_OK)


from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

class UserDeleteView(DeleteView):
   model = CustomUser
   success_url = reverse_lazy("users-list")

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request, username):
  try:
      user = CustomUser.objects.get(username=username)
  except CustomUser.DoesNotExist:
      return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

  user.delete()
  return Response({'message': 'User deleted successfully.'}, status=status.HTTP_200_OK)


@api_view(['GET'])
# @permission_classes([IsAuthenticated,IsAdminOrSuperAdmin])
def list_users(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Record
from .serializers import RecordSerializer
from django.core.exceptions import ObjectDoesNotExist

@csrf_exempt
def record_list(request):
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def record_detail(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return JsonResponse({'error': 'Record not found'}, status=404)

    if request.method == 'GET':
        serializer = RecordSerializer(record)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RecordSerializer(record, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        record.delete()
        return JsonResponse({'message': 'Record deleted successfully'}, status=204)
    
# from django.http import JsonResponse

# @csrf_exempt
# def record_create(request):
#     if request.method == 'POST':
#         # data = JSONParser().parse(request) 
#         serializer = RecordSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
#     else:
#         return Response({'error': 'Invalid request method'}, status=405)


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_405_METHOD_NOT_ALLOWED
)

from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def record_create(request):
    user = request.user

    if user.role != CustomUser.MANAGER:
        return Response({'error': 'Only managers can create records.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        data = request.data
        serializer = RecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'DELETE'])
def delete_record(request, pk):
    if request.method == 'GET':
        try:
            records = Record.objects.all()
            serializer = RecordSerializer(records, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Record.DoesNotExist:
            return Response({'error': 'No records found'}, status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'DELETE':
        try:
            record = Record.objects.get(pk=pk)
        except Record.DoesNotExist:
            return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)

        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['PUT'])
def update_record(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response({'error': 'Record not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = RecordSerializer(record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
from django.db.models import Q
from .models import Record

def record_search_api(request):
    query = request.GET.get('query')  # Assuming search query is passed as a query parameter

    if query:
        # Perform the search using OR condition on multiple fields
        results = Record.objects.filter(
            Q(name__icontains=query) |
            Q(internal_links__icontains=query) |
            Q(external_links__icontains=query)
        ).values()  # Retrieve the filtered results as a list of dictionaries
    else:
        results = Record.objects.values()  # Return all records if no search query is provided

    return JsonResponse({'results': list(results)})


