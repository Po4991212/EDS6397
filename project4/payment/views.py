from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Invoice
from .forms import PaymentForm
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Payment

# Create your views here.
@login_required
def make_payment(request, invoice_id):
    invoice = get_object_or_404(Invoice, pk=invoice_id)
    booking = invoice.booking

    if request.method == 'POST':
        form = PaymentForm(request.POST, initial={'invoice': invoice})
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount <= 0:
                messages.error(request, 'Payment amount must be greater than zero.')
                return redirect('payment:make_payment', invoice_id=invoice.id)
            if amount > invoice.total_amount:
                messages.error(request, 'Partial payment exceeds total invoice amount.')
                return redirect('payment:make_payment', invoice_id=invoice.id)
            
            payment = Payment.objects.create(
                invoice=invoice,
                user=request.user,
                amount=form.cleaned_data['amount'],
                payment_date=timezone.now(),
                payment_method='Credit Card'
            )

            invoice.total_amount -= payment.amount
            invoice.save()

            if invoice.total_amount==0:
                booking.status = "paid"
                booking.save()

            payment.save()
            messages.success(request, 'Payment submitted successfully.')
            return redirect('invoice:invoice-detail', invoice_id=invoice.id)
    else:
        
        form = PaymentForm(initial={'invoice': invoice})

    return render(request, 'payment/make-payment.html', {'form': form, 'invoice': invoice})