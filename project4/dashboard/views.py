from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from booking.models import Booking
from tour.models import Tour
from hotel.models import Hotel
from flight.models import Flight
from review.models import Review
from django.db.models import Avg, OuterRef, Subquery
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

@login_required
def index(request):
    tours = Tour.objects.all()
    hotels = Hotel.objects.all()
    flights = Flight.objects.all()
    bookings = Booking.objects.all()

    context = {
        'tours': tours,
        'hotels': hotels,
        'flights': flights,
        'bookings': bookings
    }
    return render(request, 'dashboard/agent_dashboard.html', context)

@login_required
def htmx_list_service(request, service_type):
    tours = Tour.objects.all()
    hotels = Hotel.objects.all()
    flights = Flight.objects.all()
    bookings = Booking.objects.all()
    booking_status = Booking.BOOKING_STATUS_CHOICES
    booking_context = {
        'bookings': bookings,
        'booking_status': booking_status
    }

    if service_type=='flight':
        flights = Flight.objects.all()
        return render(request, 'partials/dashboard_flight.html', {'flights': flights})
    elif service_type=='hotel':
        return render(request, 'partials/dashboard_hotel.html', {'hotels': hotels})
    elif service_type=='tour':
        return render(request, 'partials/dashboard_tour.html', {'tours': tours})
    else:
        return render(request, 'partials/dashboard_booking.html', {'booking_context': booking_context})
    
@login_required
def filter_bookings(request):
    status = request.GET.get('status', 'all')
    if status != 'all':
        bookings = Booking.objects.filter(status=status)
    else:
        bookings = Booking.objects.all()
    booking_context={
        'bookings': bookings,
    }
    return render(request, 'partials/booking_results.html', {'booking_context': booking_context})
    
@login_required
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'partials/dashboard_review.html', {'reviews': reviews})

@login_required
def reply_review(request, review_id):
    if request.method != 'POST':
        return HttpResponseBadRequest("Invalid method")
    
    rev = Review.objects.get(id=review_id)
    reply_text = request.POST.get('reply-comment')

    if not reply_text:
        return HttpResponseBadRequest("Reply text is required")

    reply = Review.objects.create(
        user=request.user,
        rating=0,
        comment=reply_text,
        content_type=rev.content_type,
        object_id=rev.object_id,
        parent=rev
    )

    if 'HX-Request' in request.headers:
        # Return only the partial HTML needed to update the page
        return render(request, 'partials/review_replies.html', {'replies': rev.replies.all()})
    else:
        # Redirect back to a full page that shows the review, typically the review detail page
        return HttpResponseRedirect(reverse('dashboard:index'))

@login_required
def filter_flights(request):
    sort = request.GET.get('select', '1')
    flights = None

    if sort == '2':
        flights = Flight.objects.all().order_by('-flight_date')
    elif sort == '3':
        flights = Flight.objects.all().order_by('flight_date')
    else:
        flights = Flight.objects.all()

    return render(request, 'partials/flights_table.html', {'flights': flights})

@login_required
def filter_tours(request):
    sort = request.GET.get('select', '1')
    tours = None

    if sort == '2':
        tours = Tour.objects.all().order_by('-price')
    elif sort == '3':
        tours = Tour.objects.all().order_by('price')
    else:
        tours = Tour.objects.all()

    return render(request, 'partials/tours_table.html', {'tours': tours})

@login_required
def filter_hotels(request):
    sort = request.GET.get('select', '1')
    hotels = None

    if sort == '2':
        hotel_content_type = ContentType.objects.get_for_model(Hotel)
        reviews = Review.objects.filter(
            content_type=hotel_content_type,
            object_id=OuterRef('pk')  
        ).values('object_id').annotate(avg_rating=Avg('rating')).values('avg_rating')

        hotels = Hotel.objects.annotate(
            average_rating=Subquery(reviews[:1])  # Ensures it fetches the avg rating per hotel
        ).order_by('-average_rating')
    elif sort == '3':
        hotels = Hotel.objects.all().order_by('-total_rooms')
    else:
        hotels = Hotel.objects.all()

    return render(request, 'partials/hotels_table.html', {'hotels': hotels})