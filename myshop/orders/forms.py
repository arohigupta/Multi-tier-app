# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T16:50:54-07:00
# @Email:  agupta@juniper.net
# @Filename: forms.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T16:54:17-07:00

from django import forms
from .models import Order
'''
This file is used to create a new order form. A Checkout service follows the following order:
1) present user with the form which asks for users personal data: myshop/orders/forms.py
2) Create an order instance: myshop/orders/views.py
'''
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
