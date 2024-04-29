from django.db import models
from datetime import datetime, timedelta
# from django.utils.timezone import now


# Create your models here.
class Flight(models.Model):
    airline = models.CharField(max_length=50)
    flight_date = models.DateField()
    flight_time = models.TimeField()
    departure_city = models.CharField(max_length=20)
    arrival_city = models.CharField(max_length=20)
    duration = models.DecimalField(max_digits=4, decimal_places=2)
    total_seats = models.IntegerField()
    booked_seats = models.IntegerField(default=0)     
    fare = models.DecimalField(max_digits=5, decimal_places=2)

    def calculate_arrival_datetime(self):
        # Convert duration to a timedelta
        # Note: duration is assumed to be in hours
        duration_hours = int(self.duration)
        duration_minutes = int((self.duration - duration_hours) * 60)
        duration_td = timedelta(hours=duration_hours, minutes=duration_minutes)

        # Combine the flight_date and flight_time into a datetime
        departure_datetime = datetime.combine(self.flight_date, self.flight_time)

        # Calculate the arrival datetime
        arrival_datetime = departure_datetime + duration_td
        return arrival_datetime
    
    def available_seats(self):
        """Returns the number of available seats on the flight."""
        return self.total_seats - self.booked_seats
    
    def __str__(self):
        return f'{self.airline} Flight from {self.departure_city} to {self.arrival_city}'
