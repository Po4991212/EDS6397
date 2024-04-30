from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('htmx_list_service/<str:service_type>/', views.htmx_list_service, name='htmx_list_service'),
    path('filter-bookings/', views.filter_bookings, name='filter_bookings'),
    path('review-list/', views.review_list, name='review_list'),
    path('reply-review/<int:review_id>/', views.reply_review, name='reply_review'),
    path('flight-filter/', views.filter_flights, name='filter_flights'),
    path('tour-filter/', views.filter_tours, name='filter_tours'),
    path('hotel-filter/', views.filter_hotels, name='filter_hotels'),
    path('create-user/', views.create_user, name='create_user'),
    path('user-detail/<int:user_id>/', views.user_detail, name='user_detail'),
    path('edit-user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete-user/<int:user_id>/', views.user_delete, name='user_delete'),
]