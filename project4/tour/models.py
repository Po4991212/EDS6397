from django.db import models

# Create your models here.
class Tour(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    destination = models.CharField(max_length=30)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    max_guests = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.description[:50]}... on {self.date}"
