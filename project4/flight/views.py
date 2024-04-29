from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Flight
from review.models import Review
from django.contrib.contenttypes.models import ContentType


# Create your views here.

@login_required
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight/flight-list.html', {'flights': flights})

@login_required
def flight_detail(request, id):
    flight = get_object_or_404(Flight, pk=id)
    reviews = Review.objects.filter(
        content_type=ContentType.objects.get_for_model(Flight),
        object_id=id
    )
    context = {
        'flight': flight,
        'reviews': reviews
    }

    return render(request, 'flight/flight-detail.html', context)

