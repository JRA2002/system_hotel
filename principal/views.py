from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView, UpdateView, FormView
from .models import Room, Reservation, Customer
from django.urls import reverse_lazy
from datetime import datetime
from . forms import ReservationForm

def home(request):
    if request.method == 'GET':
        return render(request,'principal/home.html')
    else:
        return render(request,'principal/home.html')
    
def search_results(request):
    if request.method == 'GET':
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')
        guests = request.GET.get('guests')

        check_in = datetime.strptime(check_in, '%Y-%m-%d').date()
        check_out = datetime.strptime(check_out, '%Y-%m-%d').date()
        num_days = (check_out - check_in).days
        available_rooms = Room.objects.filter(available=True)
        booked_rooms = Reservation.objects.filter(
            check_in__lte=check_out,
            check_out__gt=check_in
        ).values_list('room__num_room', flat=True)
        available_rooms = available_rooms.exclude(id__in=booked_rooms)
        print(available_rooms)
        available_rooms_list = [
            {'num_room': room.num_room, 'type_room': room.type_room, 'price': room.price,'num_days':num_days, 'available': room.available, 
            'total_price' : room.price * num_days}
            for room in available_rooms
        ]
        available_room_types = available_rooms.values_list('type_room', flat=True).distinct()
        
        request.session['reservation_context'] = {
            'check_in': str(check_in),
            'check_out': str(check_out),
            'guests': guests,
           # 'available_rooms': available_rooms_list,#user session
            #'available_room_types': available_room_types, # user session
        }
        return render(request,"principal/results.html", {'available_rooms': available_rooms_list})
    return render(request, 'principal/home.html')
        
def make_res(request):
    context = request.session.pop('reservation_context', None)
    return render(request, 'principal/results.html', context)

class HomeView(FormView):
    template_name = 'principal/home.html'  
    form_class =  ReservationForm
    success_url = 'principal/results.html'     

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)