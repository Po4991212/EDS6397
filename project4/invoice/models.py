from django.db import models
from django.conf import settings
from django.db import models

class Invoice(models.Model):
    booking_date = models.DateField()
    booking = models.OneToOneField('booking.Booking', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    promotion = models.ForeignKey('promotion.Promotion', on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id}"
    
    # def remaining_balance(self):
    #     total_paid = sum(payment.amount for payment in self.payment_set.all())
    #     return max(self.total_amount - total_paid, 0)