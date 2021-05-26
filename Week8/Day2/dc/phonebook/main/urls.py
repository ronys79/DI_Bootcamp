from django.urls import path
from . import views

urlpatterns = [
    path('name/<str:first_name>/', views.name, name='name'),
    path('phone/<int:pn>/', views.phone, name='phone')
]