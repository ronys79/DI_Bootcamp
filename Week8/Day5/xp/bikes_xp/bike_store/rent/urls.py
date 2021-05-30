from django.contrib import admin
from django.urls import path, include
from . import views

# The app should have the following URLs:
# /rent/rental/ - show a list of all rentals, unreturned first, 
# then ordered by date ascending (earliest first)

urlpatterns = [
    path('rental', views.rental_view, name = 'rental_view'),
    path('rental/<int:rental_id>', views.rentalrental_by_id, name = 'rental_by_id')
]
