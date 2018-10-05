# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:34:34-07:00
# @Email:  agupta@juniper.net
# @Filename: context_processors.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T15:35:35-07:00

from .cart import Cart

def cart(request):
    return {'cart': Cart(request) }
