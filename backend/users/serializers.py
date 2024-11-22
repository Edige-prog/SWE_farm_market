from rest_framework import serializers
from .models import User, UserRoles

class UserSerializer(serializers.ModelSerializer):
    role_display = serializers.CharField(source='get_role_display', read_only=True)  # Display role label

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone', 'password', 'role', 'role_display', 'is_active']
        extra_kwargs = {
            'password': {'write_only': True},  # Hide password in responses
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            phone=validated_data['phone'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user
