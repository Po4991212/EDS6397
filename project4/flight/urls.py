from django.urls import path
from . import views

app_name = 'flight'

urlpatterns = [
    path('', views.flight_list, name='flight_list'),
    path('flight/<int:id>/', views.flight_detail, name='flight_detail'),
]