from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def view_name(request):
	return HttpResponse('<h1>Home page<h1>')

def rental_view(request):
	rental = Rental.objects.all()
	context = {"rental":rental}
	return render(request, 'rental.html', context)

def rental_by_id(request):
	data = Rental.objects.get(id =rental_id)
	return render(request, 'rental_by_id.html', {'data': data})



# The app should have the following URLs:
# /rent/rental/ - show a list of all rentals, unreturned first, 
# then ordered by date ascending (earliest first)

