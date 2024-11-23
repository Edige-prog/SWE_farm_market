from rest_framework import serializers
from .models import Farmer, Farm
from users.serializers import UserSerializer

class FarmerSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Nested serializer

    class Meta:
        model = Farmer
        fields = ['id', 'user', 'balance']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return Farmer.objects.create(user=user, **validated_data)

class FarmSerializer(serializers.ModelSerializer):
    farmer = FarmerSerializer(read_only=True)  # Nested farmer serializer
    farmer_id = serializers.PrimaryKeyRelatedField(
        queryset=Farmer.objects.all(), write_only=True, source='farmer'
    )

    class Meta:
        model = Farm
        fields = ['id', 'farmer', 'farmer_id', 'farm_name', 'location', 'farm_size', 'is_active', 'created_at']