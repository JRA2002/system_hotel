from .models import Reservation
from django import forms

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['check_in', 'check_out', 'guests']

class ReservationFormWOM(forms.Form):
    check_in = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))
    check_out = forms.DateField( widget=forms.DateInput(attrs={'type': 'date'}))
    guests = forms.IntegerField(min_value=1, max_value=4)
    