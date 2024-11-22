from django.urls import path
from .views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list'),  # List all users, create a user
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),  # Retrieve, update, or delete a user by ID
]