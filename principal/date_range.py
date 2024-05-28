from typing import Any
from .models import Room
import datetime
from datetime import timedelta

class DateRangeMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request)
        response = self.get_response(request)
        return response
    
    def process_view(self, request, view_func, view_args, view_kargs):
        if request:
            today = datetime.date.today()
            rooms = Room.objects.all()
            for room in rooms:
                if room.check_out:
                    room.check_out = room.check_out + timedelta(days=10)
                    print(today)
                    print(room.check_out)
                    if room.check_out > today:
                        room.avaliable = False
                        room.save()