from django.urls import path
from .views import make_payment

app_name = 'payment'

urlpatterns = [
    path('payment/<int:invoice_id>/', make_payment, name='make_payment'),
]


# from django.urls import path
# from . import views

# app_name = 'invoice'

# urlpatterns = [
#     path('', views.invoice_list, name='invoice_list'),
#     path('invoice-detail/<int:invoice_id>', views.invoice_detail, name='invoice-detail'),
# ]