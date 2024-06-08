from .models import Reservation, Customer
from django import forms

class ReservationForm(forms.ModelForm):
    check_in = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'guests']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'last_name', 'email', 'phone']
    