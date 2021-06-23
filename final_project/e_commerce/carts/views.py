from django.shortcuts import get_object_or_404, render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
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
    current_user = request.user
    # product variation
    color = request.GET['color']
    size = request.GET['size']
    # get the product
    product = Product.objects.get(id=product_id)
    # if user is authenticated
    if current_user.is_authenticated:
        cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
        
        # this puts the product inside the cart and the product becomes cart item and can have multiple cart items  

        cartitem, created = cart.cartitem_set.get_or_create(product=product, user=current_user)
        if not created:
            cartitem.quantity +=1
            cartitem.save()

        return redirect('cart')

    # if user is not authenticated
    else:
        cart = Cart.objects.get_or_create(cart_id=_cart_id(request))[0]
        
        # this puts the product inside the cart and the product becomes cart item and can have multiple cart items  

        cartitem, created = cart.cartitem_set.get_or_create(product=product)
        if not created:
            cartitem.quantity +=1
            cartitem.save()

        return redirect('cart')
        # return redirect('product_detail', product.category.slug, product.slug)
    
def remove_cart(request, product_id, cart_item_id):

    product = get_object_or_404(Product, id=product_id)
    try:
        if request.user.is_authenticated:
            cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    except:
        pass
    return redirect('cart')


def remove_cart_item(request, product_id, cart_item_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    if request.user.is_authenticated:
        cart_item = CartItem.objects.get(product=product, user=request.user, id=cart_item_id)
    else:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_item = CartItem.objects.get(product=product, cart=cart, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

def cart(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2 * total)/100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass #just ignore

    context = {
        'total': total,
        'quantity': quantity,
        'cart_items': cart_items,
        'tax'       : tax,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request, total=0, quantity=0, cart_items=None):
    try:
        tax = 0
        grand_total = 0
        if request.user.is_authenticated:
            cart_items = CartItem.objects.filter(user=request.user, is_active=True)
        else:
            cart = Cart.objects.get(cart_id=_cart_id(request))
            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            # taking cart object by its id
            # here we have cart items so that we can take total of each quantity and price
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

    return render(request, 'store/checkout.html', context)