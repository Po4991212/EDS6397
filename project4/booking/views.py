from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from .forms import BookingForm, BookingUpdateForm
from flight.models import Flight
from invoice.models import Invoice
from hotel.models import Hotel
from tour.models import Tour
from review.models import Review
from datetime import datetime
from .models import Booking
from promotion.models import Promotion
from django.db import transaction
from django.contrib import messages


@login_required
def create_booking(request, service_type, service_id):
    # Mapping of service types to their corresponding models
    service_models = {
        'flight': Flight,
        'hotel': Hotel,
        'tour': Tour,
    }

    # Ensure that the service type is one of the supported types
    if service_type not in service_models:
        return render(request, '404.html', status=404)  # Render a 404 page if service type is not supported

    # Retrieve the specific service based on service_type and service_id
    service_model = service_models[service_type]
    service_instance = get_object_or_404(service_model, pk=service_id)

    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = BookingForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                # Create a new booking instance, without saving it to the database yet
                booking = form.save(commit=False)
                booking.user = request.user

                # Update the relevant fields based on the service type
                if service_type == 'flight':
                    service_instance.booked_seats += booking.num_of_guests
                    service_instance.save()
                    booking.flight = service_instance
                elif service_type == 'hotel':
                    service_instance.total_rooms -= 1  # Reduce available rooms
                    service_instance.save()
                    booking.hotel = service_instance
                elif service_type == 'tour':
                    if service_instance.max_guests < booking.num_of_guests:
                        raise ValueError("Number of guests exceeds the maximum allowed for this tour.")
                    service_instance.save()
                    booking.tour = service_instance

                booking.status = 'payment pending'  # Default status for new booking
                booking.booking_date = datetime.today()
                booking.save()  # Save the booking to the database
                promo_code = request.POST.get('promo_code')
                try:
                    promotion = Promotion.objects.get(code=promo_code)
                except Promotion.DoesNotExist:
                    promotion = None
                base_cost = booking.total_amount
                if promotion:
                    discount_amount = base_cost * promotion.discount_percentage
                    total_invoice = base_cost - discount_amount
                else:
                    total_invoice = base_cost

                invoice = Invoice.objects.create(
                    user=request.user,
                    booking=booking,
                    booking_date=booking.booking_date,
                    total_amount=total_invoice,
                    promotion_id=promotion.id if promotion else None
                )
                invoice.save()
                
            return redirect('invoice:invoice-detail', invoice_id=invoice.id)
    else:
        # If this is a GET request, create the default form
        form = BookingForm()
  
    arrival_time = service_instance.calculate_arrival_datetime if service_type == 'flight' else None
    
    # Render the create booking page with the booking form and service information
    context = {
        'form': form,
        'service': service_instance,
        'service_type': service_type,
        'arrival_time': arrival_time
    }
    return render(request, 'booking/create_booking.html', context)

@login_required
def list_booking(request):
    today = now().date()  # Today's date

    # Filter bookings into current and past based on the reservation_end_date
    current_bookings = Booking.objects.filter(
        user=request.user, 
        reservation_end_date__gte=today
    ).order_by('reservation_date')

    past_bookings = Booking.objects.filter(
        user=request.user, 
        reservation_end_date__lt=today
    ).order_by('-reservation_date')

    context = {
        'current_bookings': current_bookings,
        'past_bookings': past_bookings
    }
    

    return render(request, 'booking/list_booking.html', context)

@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    invoice = get_object_or_404(Invoice, booking=booking)  # Ensure there is an invoice for this booking


    # if not request.user.is_authenticated or (booking.user != request.user and not request.user.is_staff):
    #     messages.error(request, "You do not have permission to update this booking.")
    #     return redirect('some-error-page')
    if request.method == 'POST':
        form = BookingUpdateForm(request.POST, instance=booking)
        
        if form.is_valid():

            booking = form.save()
            if not booking.flight:
                flight_id = request.POST.get('flight_id')
                if flight_id:
                    booking.flight = Flight.objects.get(id=flight_id)

            if not booking.hotel:
                hotel_id = request.POST.get('hotel_id')
                if hotel_id:
                    booking.hotel = Hotel.objects.get(id=hotel_id)

            if not booking.tour:
                tour_id = request.POST.get('tour_id')
                if tour_id:
                    booking.tour = Tour.objects.get(id=tour_id)
            invoice.total_amount = booking.total_amount
            invoice.save()
           

            messages.success(request, "Booking updated successfully.")
            return redirect('booking:detail_booking', booking_id=booking.id)
        
    else:
        form = BookingUpdateForm(instance=booking)
    
    return render(request, 'booking/update_booking.html', {'form': form, 'booking': booking})

@login_required
def detail_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    context = {
        'booking': booking,
        'hotel': booking.hotel,
        'flight': booking.flight,
        'tour': booking.tour,
    }
    return render(request, 'booking/detail_booking.html', context)

def get_service_details(request, service_type, service_id):
    context = {}
    if service_type == 'flight':
        context['service'] = Flight.objects.filter(id=service_id).first()
    elif service_type == 'hotel':
        context['service'] = Hotel.objects.filter(id=service_id).first()
    elif service_type == 'tour':
        context['service'] = Tour.objects.filter(id=service_id).first()

    return render(request, 'partials/service_details.html', context)

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    invoice = get_object_or_404(Invoice, booking=booking)
    if booking.status == 'cancelled':
        messages.error(request, "Booking has already been cancelled.")
        return redirect('booking:list_booking')
    if booking.status == 'completed':
        messages.error(request, "Booking has already been completed.")
        return redirect('booking:list_booking')
    if booking.status == 'payment pending':
        messages.error(request, "Booking has not been paid for.")
        return redirect('booking:list_booking')
    with transaction.atomic():
        booking.status = 'cancelled'
        booking.save()
        invoice.status = 'cancelled'
        invoice.save()
        if booking.flight:
            booking.flight.booked_seats -= booking.num_of_guests
            booking.flight.save()
        if booking.hotel:
            booking.hotel.total_rooms += 1
            booking.hotel.save()
    messages.success(request, "Booking cancelled successfully.")
    return redirect('booking:list_booking')
