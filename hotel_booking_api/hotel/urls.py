# urls.py

from django.urls import path
from .views import *

urlpatterns = [
    path('hotels/', HotelListCreateView.as_view(), name='hotel-list-create'),
    path('hotels/<int:pk>/', HotelDetailView.as_view(), name='hotel-detail'),
    path('rooms/', RoomListCreateView.as_view(), name='room-list-create'),
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),
    path('hotels_search/', HotelSearchView.as_view(), name='hotel-search'),
    path('rooms_search/', RoomSearchView.as_view(), name='room-search'),
    path('room_booking/', RoomBookingView.as_view(), name='room-booking'),
    path('user_room_booking/', UserRoomBookingListView.as_view(), name='user-room-booking-list'),
     path('cancel_booking/<int:booking_id>/', CancelBookingView.as_view(), name='cancel-booking'),
]
