from django import forms
from .models import Hotel

class HotelBookingForm(forms.Form):
    check_in_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    check_out_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    number_of_guests = forms.IntegerField(min_value=1)

    class Meta:
        model = Hotel
        fields = ['check_in_date', 'check_out_date', 'number_of_guests']
