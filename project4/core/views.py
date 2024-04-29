from django.shortcuts import render
from django.db.models import Min  # Import the Min function
from hotel.models import Hotel
from tour.models import Tour
from flight.models import Flight


# Create your views here.
def index(request):
    lowest_rate = Hotel.objects.aggregate(Min('nightly_rate'))['nightly_rate__min']
    lowest_fare = Flight.objects.aggregate(Min('fare'))['fare__min']
    lowest_price = Tour.objects.aggregate(Min('price'))['price__min']
    context = {
        'lowest_rate': lowest_rate,
        'lowest_fare': lowest_fare,
        'lowest_price': lowest_price
    }

    return render(request, 'core/index.html', context)

# def search_service(request):
#     return render(request, 'core/search.html')