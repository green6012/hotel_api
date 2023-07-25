
from django.db import models
from django.contrib.auth.models import User
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    

    def __str__(self):
        return self.name

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    bed_count = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"{self.hotel.name} - Room {self.room_number}"
