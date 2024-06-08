from django.db import models
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
import datetime
from datetime import timedelta

# Create your models here.

class Room(models.Model):

    TYPES_ROOM  = [
        ('double', 'Double'),
        ('king', 'King'),
        ('two_double', 'Two Double'),
        ('suite', 'Suite')
    ]
    num_room = models.IntegerField(unique=True, default=0)
    type_room = models.CharField(choices=TYPES_ROOM, max_length=10, default=0)
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='principal/room',default='principal/room/default.jpeg')

    def __str__(self):
        return self.type_room
    
    def mark_as_booked(self):
        self.available = False
        self.save()
    
    def mark_as_available(self):
        self.available = True
        self.save()

class Customer(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(default=2)

    def __str__(self):
        return f"Reservation for {self.customer} - Room No {self.room.num_room}"
    
        

    