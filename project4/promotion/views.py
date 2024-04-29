from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Promotion



# Create your views here.

@login_required
def promotion_list(request):
    promotions = Promotion.objects.all()
    return render(request, 'promotion/promotion-list.html', {'promotions': promotions})



