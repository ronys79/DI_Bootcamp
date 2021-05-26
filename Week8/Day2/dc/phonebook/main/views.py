from django.shortcuts import render
from .models import Phonebook

# Create your views here.
def name(request, first_name):
    data = Phonebook.objects.get(name=first_name)
    return render(request, 'person.html', {'data': data})
    
def phone(request, pn):
    data = Phonebook.objects.get(phone_number=pn)
    return render(request, 'person.html', {'data': data})