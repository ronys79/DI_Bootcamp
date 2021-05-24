from django.urls import path #path function
from . import views # . is shorthand for the current directory


# one urlpattern per line
urlpatterns = [
    path('family/<int:fam_id>', views.family, name='family'),
    path('animal/<int:animal_id>', views.animal, name='animal'),
]