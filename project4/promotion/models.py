from django.db import models

# Create your models here.
class Promotion(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
    discount_percentage = models.DecimalField(max_digits=3, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()