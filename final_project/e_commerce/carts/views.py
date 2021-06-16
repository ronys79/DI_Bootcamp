from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Cart, CartItem
from store.models import Product


def _cart_id(request):
    # get session id key and converts it into cart id
    cart = request.session.session_key
    # if no id creates on 
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    color = request.GET['color']
    size = request.GET['size']
    # get the product
    product = Product.objects.get(id=product_id)
    cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
    
    # this puts the product inside the cart and the product becomes cart item and can have multiple cart items  

    cartitem, created = cart.cartitem_set.get_or_create(product=product)
    if not created:
        cartitem.quantity +=1
        cartitem.save()

    return redirect('cart')
    # return redirect('product_detail', product.category.slug, product.slug)
    
def remove_cart(request, product_id):
    # get the cart details
    cart = Cart.objects.get(cart_id=_cart_id(request))
    # if object is presnt it will return if not 404
    product = get_object_or_404(Product, id=product_id)
    # brings the cart item
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, product_id):
    # get the cart details
    cart = Cart.objects.get(cart_id=_cart_id(request))
    # if object is presnt it will return if not 404
    product = get_object_or_404(Product, id=product_id)
    # brings the cart item
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        # taking cart object by its id
        cart = Cart.objects.get(cart_id=_cart_id(request))
        # here we have cart items so that we can take total of each quantity and price
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity

        tax = (17 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #ignore if doesnt exists

# alll data to use in cart template
    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax' : tax,
        'grand_total' : grand_total,
    }

    return render(request, 'store/cart.html', context)