from django.urls import path
from . import views

app_name = 'invoice'

urlpatterns = [
    path('', views.invoice_list, name='invoice_list'),
    path('invoice-detail/<int:invoice_id>', views.invoice_detail, name='invoice-detail'),
]