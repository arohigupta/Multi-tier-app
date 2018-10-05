# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:44:43-07:00
# @Email:  agupta@juniper.net
# @Filename: views.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T17:14:29-07:00

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from .tasks import order_created
from cart.cart import Cart

'''
1) Create an order: Check current status of the cart. Redirect and clear the cart.
'''
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart,
                                                        'form': form})
