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
]
