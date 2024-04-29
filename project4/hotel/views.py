from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Hotel
from .forms import HotelBookingForm
from review.models import Review
from django.contrib.contenttypes.models import ContentType

@login_required
def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel/hotel-list.html', {'hotels': hotels})

@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = HotelBookingForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            return render(request, 'hotel/booking_confirmation.html', {'hotel': hotel})
    else:
        form = HotelBookingForm(instance=hotel)

    return render(request, 'hotel/book_hotel.html', {'form': form, 'hotel': hotel})

@login_required
def hotel_detail(request, id):
    hotel = get_object_or_404(Hotel, pk=id)
    reviews = Review.objects.filter(
        content_type=ContentType.objects.get_for_model(Hotel),
        object_id=id
    )
    context = {
        'hotel': hotel,
        'reviews': reviews
    }
    return render(request, 'hotel/hotel-detail.html', context)