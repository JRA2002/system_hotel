from django.db import models
from django.db.models.signals import post_delete,post_save
from django.dispatch import receiver
import datetime
from datetime import timedelta

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    avaliable = models.BooleanField(default=True)
    check_in = models.DateField(blank=True, null=True)
    check_out = models.DateField(blank=True, null=True)
    max_guests = models.IntegerField()
    description = models.TextField(help_text="Enter a brief description of the room")

    def __str__(self):
        return self.name
    
    

    