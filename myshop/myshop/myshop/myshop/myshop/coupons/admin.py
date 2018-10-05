# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T12:15:34-07:00
# @Email:  agupta@juniper.net
# @Filename: admin.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T12:24:41-07:00

from django.contrib import admin
from .models import Coupon
# Register your models here.
'''
Logic to apply coupons for user:
1) user adds product to the cart
2) User enters coupon code
3) admin view checks validity
4) if valid; save it in cart with updated value (session)
5) checkout.
'''


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

admin.site.register(Coupon, CouponAdmin)
