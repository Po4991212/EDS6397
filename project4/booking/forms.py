from django import forms
from .models import Booking
from hotel.models import Hotel
from tour.models import Tour
from flight.models import Flight

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'reservation_date', 'reservation_end_date', 
            'num_of_guests', 'traveler_fname', 'traveler_lname'
        ]
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'num_of_guests': forms.NumberInput(attrs={'class': 'form-control'}),
            'traveler_fname': forms.TextInput(attrs={'class': 'form-control'}),
            'traveler_lname': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BookingUpdateForm(forms.ModelForm):
    flight = forms.ModelChoiceField(
        queryset=Flight.objects.all(),  # Use the custom manager method
        required=False,
        label="Current Flight booking",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="No Flight Selected"
    )
    hotel = forms.ModelChoiceField(
        queryset=Hotel.objects.all(),  # Assuming no specific availability checks are needed
        required=False,
        label="Current Hotel booking",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="No Hotel Selected"
    )
    tour = forms.ModelChoiceField(
        queryset=Tour.objects.all(),  # Assuming no specific availability checks are needed
        required=False,
        label="Current Tour Booking",
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="No Tour Selected"
    )
    reservation_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    reservation_end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    num_of_guests = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    traveler_fname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    traveler_lname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = Booking
        fields = ['reservation_date', 'reservation_end_date',
            'num_of_guests', 'traveler_fname', 'traveler_lname', 'flight', 'hotel', 'tour']