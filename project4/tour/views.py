from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TourBookingForm
from .models import Tour
from review.models import Review
from django.contrib.contenttypes.models import ContentType

# Create your views here.

@login_required
def tour_list(request):
    tours = Tour.objects.all()
    return render(request, 'tour/tour-list.html', {'tours': tours})

@login_required
def book_tour(request, tour_id):
    tour = get_object_or_404(Tour, pk=tour_id)
    if request.method == 'POST':
        form = TourBookingForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            return render(request, 'tour/booking_confirmation.html', {'tour': tour})
    else:
        form = TourBookingForm(instance=tour)

    return render(request, 'tour/book_tour.html', {'form': form, 'tour': tour})

@login_required
def tour_detail(request, id):
    tour = get_object_or_404(Tour, pk=id)
    reviews = Review.objects.filter(
        content_type=ContentType.objects.get_for_model(Tour),
        object_id=id
    )
    context = {
        'tour': tour,
        'reviews': reviews
    }
    return render(request, 'tour/tour-detail.html', context)