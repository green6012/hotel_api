from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import  SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from .serializers import HotelSerializer, RoomSerializer, RoomBookingSerializer
from user_auth import serializers
from hotel.models import Hotel, Room, RoomBooking
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


class HotelListCreateView(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class HotelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

class RoomListCreateView(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated ]

class RoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsOwnerOrReadOnly]

class HotelSearchView(ListAPIView):
    serializer_class = HotelSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')  
        return Hotel.objects.filter(name__icontains=search_query)

class RoomSearchView(ListAPIView):
    serializer_class = RoomSerializer

    def get_queryset(self):
        search_query = self.request.query_params.get('search', '')  
        return Room.objects.filter(room_number__icontains=search_query)
    
class RoomBookingView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = RoomBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserRoomBookingListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RoomBookingSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def get_queryset(self):
        user = self.request.user
        return RoomBooking.objects.filter(user=user)
    
class CancelBookingView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    def post(self, request, booking_id):
        try:
            booking = RoomBooking.objects.get(id=booking_id, user=request.user)
        except RoomBooking.DoesNotExist:
            return Response({"message": "Booking not found."}, status=status.HTTP_404_NOT_FOUND)

        if booking.is_cancelled:
            return Response({"message": "Booking has already been cancelled."}, status=status.HTTP_400_BAD_REQUEST)

        booking.is_cancelled = True
        booking.save()

        return Response({"message": "Booking has been cancelled successfully."}, status=status.HTTP_200_OK)