from django.urls import path
from . import views

app_name = 'tour'

urlpatterns = [
    path('', views.tour_list, name='tour_list'),
    path('book/<int:tour_id>/', views.book_tour, name='book_tour'),
    path('detail/<int:id>/', views.tour_detail, name='tour_detail')
]