# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T12:15:34-07:00
# @Email:  agupta@juniper.net
# @Filename: views.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T13:14:40-07:00

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupon
from .forms import CouponApplyForm
# Create your views here.

'''
This is a post only method.
1) check if the form is valid.
2) get coupon objects (case sensitive; must be within range, and should be active)
3) install in user session/
4) coupon apply view. 

'''

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                    valid_from__lte=now,
                                    valid_to__gte=now,
                                    active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
