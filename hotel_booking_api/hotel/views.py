from rest_framework.generics import ListAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import  SAFE_METHODS, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions
from .serializers import HotelSerializer, RoomSerializer
from user_auth import serializers
from hotel.models import Hotel, Room
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