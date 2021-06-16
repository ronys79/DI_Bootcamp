from django.shortcuts import render
from store.models import Product

def home(request):
# filter out the not available products, can adjust to out of stock as well
    products = Product.objects.all().filter(is_available=True)

    context = {
        'products': products
    }

    return render(request, 'home.html', context)