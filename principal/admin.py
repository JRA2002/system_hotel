from django.contrib import admin
from .models import Room, Customer, Reservation
# Register your models here.

admin.site.register(Room)
admin.site.register(Customer)
admin.site.register(Reservation)
