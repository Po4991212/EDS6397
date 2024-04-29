from django.urls import path
from . import views

app_name = 'review'

urlpatterns = [
    # path('reviews/', views.review_list, name='review_list'),
    # path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    # path('reviews/add/', views.review_create, name='review_add'),
    # path('reviews/<int:pk>/edit/', views.review_update, name='review_edit'),
    # path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('add-review/<str:service_type>/<int:service_id>/', views.htmx_add_review, name='htmx_add_review'),
]
