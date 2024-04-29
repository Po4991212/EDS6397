from django import forms
from .models import Payment
from django.core.exceptions import ValidationError
from invoice.models import Invoice

class PaymentForm(forms.ModelForm):
    PAYMENT_CHOICES = [
        ('Credit Card', 'Credit Card'),
    ]
    
    payment_method = forms.ChoiceField(choices=PAYMENT_CHOICES, initial='Credit Card')

    class Meta:
        model = Payment
        fields = ['amount', 'payment_method','card_number', 'card_expiry', 'card_cvv', 'zip']
        widgets = {
            'card_expiry': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
            'card_number': forms.TextInput(attrs={'placeholder': '1234 5678 9012 3456', 'maxlength': '19'}),
            'card_cvv': forms.TextInput(attrs={'placeholder': '123', 'maxlength': '3'}),
            'zip': forms.TextInput(attrs={'placeholder': '12345', 'maxlength': '5'}),
        }

    def clean_card_cvv(self):
        card_cvv = self.cleaned_data.get('card_cvv')
        if len(card_cvv) != 3:
            raise ValidationError("CVV must be exactly 3 digits.")
        return card_cvv

    def clean_zip(self):
        zip_code = self.cleaned_data.get('zip')
        if len(zip_code) != 5:
            raise ValidationError("ZIP code must be exactly 5 digits.")
        return zip_code

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        invoice = self.cleaned_data.get('invoice_id')
        if invoice and invoice.remaining_balance() < amount:
            raise ValidationError("The payment amount exceeds the remaining balance.")
        return amount