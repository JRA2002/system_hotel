from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Check-in')
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Check-out')
    guests = forms.IntegerField(label='Guests', initial=1)

