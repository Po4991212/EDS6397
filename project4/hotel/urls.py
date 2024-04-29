from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
    path('book/<int:hotel_id>/', views.book_hotel, name='book_hotel'),
    path('detail/<int:id>/', views.hotel_detail, name='hotel_detail')
]