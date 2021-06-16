from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from carts.models import Cart
from category.models import Category
from carts.models import CartItem
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from carts.views import _cart_id
from django.db.models import Q


def store(request, category_slug=None):
# what to do if slug is not empty
    if category_slug != None:
        # get page or render 404
        category = get_object_or_404(Category, slug=category_slug)
        # order by function to order in pagination, set to order by id
        products = category.product_set.filter(is_available=True).order_by('id')
        paginator = Paginator(products, 6)
        #  capturing url page for paginator
        page = request.GET.get('page')
        # storing products captured above to be displayed on html
        paged_products = paginator.get_page(page)
        items_found = products.count()
        if products.count() == 0:
            return redirect('store')
    else:
        # display all products on store if slug not found so page isnt blank
        products = Product.objects.all().filter(is_available=True)
        # paginator functunality to display qnt of products
        paginator = Paginator(products, 6)
        #  capturing url page for paginator
        page = request.GET.get('page')
        # storing products captured above to be displayed on html
        paged_products = paginator.get_page(page)
        # total products displayed
        items_found = products.count()

    context = {
        'products': paged_products,
        'items_found': items_found,
    }

    return render(request, 'store/store_base.html', context)

def product_detail(request, category_slug, product_slug):
    # to get single view page
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        # check if object added to cart
        # if this query returns any object that may exiest it returns true and if false then object not in cart
        in_cart = Cart.objects.filter(cart_id=_cart_id(request), cartitem__product=single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }

    return render(request, 'store/produt_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # filtering search for now via description
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) | 
                Q(product_name__icontains=keyword) | 
                Q(price__icontains=keyword) | 
                Q(category__category_name__icontains=keyword)
                )
            items_found = products.count()

    context = {
        'products': products,
        'items_found': items_found,
        'keyword' : keyword,
    }
    return render(request, 'store/store_base.html', context)
