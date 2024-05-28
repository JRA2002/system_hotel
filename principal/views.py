from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from django.http import HttpResponse
from .forms import DateRangeForm
from .models import Room

class HomeView(TemplateView):
    template_name = 'principal/home.html'


class RoomListView(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'principal/rooms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = Room.objects.filter(avaliable=True)
        context['rooms'] = rooms
        return context

class RoomDetailView(DetailView):
    model = Room
    template_name = 'principal/detail_room.html'
    context_object_name = 'rooms'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rooms = Room.objects.filter(avaliable=True)
        context['rooms'] = rooms
        return context

