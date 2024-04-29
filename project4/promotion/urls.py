from django.urls import path
from . import views

app_name = 'promotion'

urlpatterns = [
    path('', views.promotion_list, name='promotion_list'),
]