from django.shortcuts import render, redirect
from django.views.generic import TemplateView,ListView,DetailView, UpdateView, FormView,View
from django.contrib.auth import logout
from .models import Room, Reservation, Customer
from django.urls import reverse_lazy
from datetime import datetime
from . forms import ReservationForm, CustomerForm
from django.http.response import JsonResponse # new
from django.views.decorators.csrf import csrf_exempt # new
from django.conf import settings
import stripe

class HomerView(TemplateView):
    template_name = 'homer.html'
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order
            # Other optional params include:
            # [billing_address_collection] - to display billing address details on the page
            # [customer] - if you have an existing Stripe Customer ID
            # [payment_intent_data] - capture the payment later
            # [customer_email] - prefill the email input in the form
            # For full details see https://stripe.com/docs/api/checkout/sessions/create

            # ?session_id={CHECKOUT_SESSION_ID} means the redirect will have the session ID set as a query param
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': 'prod_QIH6mcFszoDUmc',
                        'quantity': 1,
                        'currency': 'usd',
                        'price': 'price_1PRgY3IMnBjuYLYY9QgS7pTy',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("home")
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
            {'num_room': room.num_room, 'type_room': room.type_room, 'price': room.price,'num_days':num_days,'image':room.image, 'available': room.available, 
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
    
class CustomerView(FormView):
    template_name = 'principal/detail_customer.html'  
    form_class =  CustomerForm
    success_url = 'principal/results.html'     

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)
    
class ReservationView(ListView):
    model = Reservation
    template_name = 'principal/reservation_list.html'
    context_object_name = 'reservation_list'

    def get_queryset(self):
        return Reservation.objects.all()