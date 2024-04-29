from django.urls import path

from . import views

app_name = 'booking'

urlpatterns = [
    path('create/<str:service_type>/<int:service_id>/', views.create_booking, name='create_booking'),
    path('booking/', views.list_booking, name='list-booking'),
    path('detail/<int:booking_id>/', views.detail_booking, name='detail_booking'),
    path('booking/update/<int:booking_id>/', views.update_booking, name='update-booking'),
    # path('deletebooking/', views.delete_booking, name='delete_booking')
]