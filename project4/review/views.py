from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review
from flight.models import Flight
from tour.models import Tour
from hotel.models import Hotel  
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib.contenttypes.models import ContentType

# @login_required
# def review_list(request):
#     reviews = Review.objects.all()
#     return render(request, 'reviews/review_list.html', {'reviews': reviews})

# @login_required
# def review_detail(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     return render(request, 'reviews/review_detail.html', {'review': review})

# @login_required
# def review_create(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('review_list'))
#     else:
#         form = ReviewForm()
#     return render(request, 'reviews/review_form.html', {'form': form})

# @login_required
# def review_update(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == 'POST':
#         form = ReviewForm(request.POST, instance=review)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('review_detail', args=[pk]))
#     else:
#         form = ReviewForm(instance=review)
#     return render(request, 'reviews/review_form.html', {'form': form})

# @login_required
# def review_delete(request, pk):
#     review = get_object_or_404(Review, pk=pk)
#     if request.method == 'POST':
#         review.delete()
#         return HttpResponseRedirect(reverse('review_list'))
#     return render(request, 'reviews/review_confirm_delete.html', {'review': review})

@login_required
@require_POST
def htmx_add_review(request, service_type, service_id):
    # Mapping service_type to model classes
    model_map = {
        'flight': Flight,
        'hotel': Hotel,
        'tour': Tour,
    }

    if service_type not in model_map:
        return HttpResponse("Invalid service type", status=400)

    model_class = model_map[service_type]
    service_instance = get_object_or_404(model_class, pk=service_id)

    if request.method == 'POST':
        comment = request.POST.get('comment', '').strip()
        rating = request.POST.get('rating', '').strip()

        # Validate comment and rating
        if not comment:
            return HttpResponse("Comment is required", status=400)
        if not rating.isdigit() or not 0 < int(rating) <= 5:
            return HttpResponse("Rating must be between 1 and 5", status=400)

        # Create a new review
        Review.objects.create(
            user=request.user,
            content_type=ContentType.objects.get_for_model(model_class),
            object_id=service_id,
            comment=comment,
            rating=int(rating)
        )

    # Retrieve all reviews associated with this service
    reviews = Review.objects.filter(
        content_type=ContentType.objects.get_for_model(model_class),
        object_id=service_id
    )

    # Render the partial with the reviews
    return render(request, 'partials/htmx_add_review.html', {'reviews': reviews})
