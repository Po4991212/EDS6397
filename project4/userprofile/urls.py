from django.urls import path

from . import views

app_name = 'userprofile'

urlpatterns = [
    path('myaccount/', views.myaccount, name='myaccount'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('list-users/', views.list_users, name='list_users'),
]