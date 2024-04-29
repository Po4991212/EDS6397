from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# Create your models here.
class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('payment pending', 'Payment Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE)
    reservation_date = models.DateField(validators=[MinValueValidator(limit_value=timezone.now().date())])
    reservation_end_date = models.DateField()
    duration = models.IntegerField()
    num_of_guests = models.IntegerField()
    traveler_fname = models.CharField(max_length=20)
    traveler_lname = models.CharField(max_length=20)
    booking_date = models.DateField()
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES)
    flight = models.ForeignKey('flight.Flight', on_delete=models.SET_NULL, null=True, blank=True)
    hotel = models.ForeignKey('hotel.Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    tour = models.ForeignKey('tour.Tour', on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status_change_date = models.DateField(null=True, blank=True)
    
    @property
    def duration(self):
        """Calculate duration of the booking."""
        return (self.reservation_end_date - self.reservation_date).days if self.reservation_end_date and self.reservation_date else 0
    
    def calculate_total_amount(self):
        """Calculate the total amount for the booking based on flight, hotel, and tour."""
        total = 0
        if self.flight:
            total += self.flight.fare * self.num_of_guests
        if self.hotel:
            total += self.hotel.nightly_rate * self.duration
        if self.tour:
            total += self.tour.price * self.num_of_guests
        return total

    def save(self, *args, **kwargs):
        """Overwrite save method to calculate total amount and track status changes."""
        self.total_amount = self.calculate_total_amount()
        if self.pk is not None:
            orig = Booking.objects.get(pk=self.pk)
            if orig.status != self.status:
                self.status_change_date = timezone.now().date()
        super(Booking, self).save(*args, **kwargs)

    def get_booking_detail(self):
        if self.hotel:
            return self.hotel.name
        elif self.flight:
            return self.flight.arrival_city
        elif self.tour:
            return self.tour.name
        return "No details" 
    