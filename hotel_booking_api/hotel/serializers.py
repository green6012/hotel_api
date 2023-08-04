from rest_framework import serializers
from .models import Hotel, Room, RoomBooking
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

class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = ['room', 'check_in_date', 'check_out_date', 'num_guests']

    def validate(self, data):
        # Kiểm tra xem phòng đã được đặt bởi người dùng khác hay chưa
        room = data['room']
        check_in_date = data['check_in_date']
        check_out_date = data['check_out_date']

        if RoomBooking.objects.filter(room=room, check_out_date__gte=check_in_date, check_in_date__lte=check_out_date).exists():
            raise serializers.ValidationError('This room is already booked for the selected dates.')
        
        return data