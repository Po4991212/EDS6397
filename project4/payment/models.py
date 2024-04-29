from django.db import models
from invoice.models import Invoice
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20)
    card_number = models.CharField(max_length=16, blank=True, null=True)
    card_expiry = models.DateField(blank=True, null=True)
    card_cvv = models.CharField(max_length=3, blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
