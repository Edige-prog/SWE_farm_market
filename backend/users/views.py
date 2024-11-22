from operator import truediv
from xmlrpc.client import Boolean

from rest_framework.permissions import AllowAny
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

# List and Create Users
class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data['username']
        new_user = User.objects.filter(username=username)
        if new_user.exists():
            return Response({'username': 'This username is already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            is_active = request.data['is_active']
        except KeyError:
            is_active = False

        obj = User.objects.create(username=username, email=request.data['email'], phone=request.data['phone'], password=request.data['password'], role=request.data['role'], is_active = is_active)
        serializer = self.get_serializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# Retrieve, Update, and Delete a User
class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# class UserListCreateAPIView(generics.CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)