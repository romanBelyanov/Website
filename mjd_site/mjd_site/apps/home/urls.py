from django.urls import path
from . import views
import food.views, hotel.views

app_name = 'home'
urlpatterns = [
    path('', views.open_lk, name='open_lk'),
    path('profile/', views.profile, name='profile'),
    path('map/', food.views.map_for_authorise, name='map_for_authorise'),
    path('hotel/', hotel.views.hotel_for_authorise, name='hotel')
]