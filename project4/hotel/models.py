from django.db import models
from datetime import timedelta
from datetime import datetime

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    total_rooms = models.IntegerField()
    nightly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} in {self.city}, Rooms: {self.total_rooms}, Price: {self.nightly_rate}"
