# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:27:25-07:00
# @Email:  agupta@juniper.net
# @Filename: views.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T15:18:22-07:00

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.cache import cache_page
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.conf import settings
from coupons.forms import CouponApplyForm
from shop.recommender import Recommender

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)
@require_POST
@cache_page(CACHE_TTL)
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:cart_detail')

@cache_page(CACHE_TTL)
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    coupon_apply_form = CouponApplyForm()
    r = Recommender()
    cart_products = [item['product'] for item in cart]
    recommended_products = r.suggest_products_for(cart_products, max_results=4)

    return render(request, 'cart/detail.html', {'cart': cart,
                                            'coupon_apply_form': coupon_apply_form,
                                            'recommended_products': recommended_products})
