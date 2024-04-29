from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

from core.views import index
from userprofile.forms import LoginForm
from userprofile.views import signup
from userprofile.views import logout_view


urlpatterns = [
    path('', index, name='index'),
    path('log-in/', views.LoginView.as_view(template_name='userprofile/login.html', authentication_form=LoginForm), name='login'),
    path('log-out/', logout_view, name='logout'),
    path('sign-up/', signup, name='signup'),
    path('admin/', admin.site.urls, name='admin'),
    path('userprofile/', include('userprofile.urls')),
    path('flight/', include('flight.urls')),
    path('tour/', include('tour.urls')),
    path('hotel/', include('hotel.urls')),
    path('booking/', include('booking.urls')),
    path('promotion/', include('promotion.urls')),
    path('invoice/', include('invoice.urls')),
    path('payment/', include('payment.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('review/', include('review.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
