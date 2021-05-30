from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def all_rentals(request):
    data = Rental.objects.all()
    return render(request, 'all_rentals.html', {'data': data})

def rental_by_id(request, rental_id):
    data = Rental.objects.get(id=rental_id)
    return render(request, 'rental_by_id.html', {'data': data})

def add_rental(request):
    if request.method == 'GET':
        form = RentalForm()
        return render(request, 'add.html', {'form': form, 'type': 'Rental'})
    elif request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            Rental.objects.create(**form.cleaned_data)
        return redirect('all_rentals')

def customer_by_id(request, customer_id):
    data = Customer.objects.get(id=customer_id)
    return render(request, 'customer_by_id.html', {'data': data})

def all_customers(request):
    data = Customer.objects.all()
    return render(request, 'all_customers.html', {'data': data})

def add_customer(request):
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'add.html', {'form': form, 'type': 'Customer'})
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(**form.cleaned_data)
        return redirect('add_customer')

def all_vehicles(request):
    data = Vehicle.objects.all()
    return render(request, 'all_vehicles.html', {'data': data})

def vehicle_by_id(request, vehicle_id):
    data = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'vehicle_by_id.html', {'data': data})

def add_vehicle(request):
    if request.method == 'GET':
        form = VehicleForm()
        return render(request, 'add.html', {'form': form, 'type': 'Vehicle'})
    elif request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            Vehicle.objects.create(**form.cleaned_data)
        return redirect('add_vehicle')