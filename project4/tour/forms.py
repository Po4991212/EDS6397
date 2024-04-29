from django import forms
from .models import Tour

class TourBookingForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'description', 'destination', 'date', 'time', 'duration', 'max_guests', 'price']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'})
        }
