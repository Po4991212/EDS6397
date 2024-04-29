from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Invoice
from booking.models import Booking
from promotion.models import Promotion
from django.utils import timezone


# Create your views here.
@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user, total_amount__gt=0).order_by('-booking_date')
    return render(request, 'invoice/invoice-list.html', {'invoices': invoices})

@login_required
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'invoice/invoice-detail.html', {'invoice':invoice})