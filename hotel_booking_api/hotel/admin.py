from django.contrib import admin

# Register your models here.
from .models import Hotel
from .models import Room

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')

class RoomAmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_number', 'bed_count','price_per_night')

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAmin)