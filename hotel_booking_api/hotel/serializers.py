from rest_framework import serializers
from .models import Hotel, Room
from .permissions import IsOwnerOrReadOnly

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
        permission_classes = [IsOwnerOrReadOnly]

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        permission_classes = [IsOwnerOrReadOnly]