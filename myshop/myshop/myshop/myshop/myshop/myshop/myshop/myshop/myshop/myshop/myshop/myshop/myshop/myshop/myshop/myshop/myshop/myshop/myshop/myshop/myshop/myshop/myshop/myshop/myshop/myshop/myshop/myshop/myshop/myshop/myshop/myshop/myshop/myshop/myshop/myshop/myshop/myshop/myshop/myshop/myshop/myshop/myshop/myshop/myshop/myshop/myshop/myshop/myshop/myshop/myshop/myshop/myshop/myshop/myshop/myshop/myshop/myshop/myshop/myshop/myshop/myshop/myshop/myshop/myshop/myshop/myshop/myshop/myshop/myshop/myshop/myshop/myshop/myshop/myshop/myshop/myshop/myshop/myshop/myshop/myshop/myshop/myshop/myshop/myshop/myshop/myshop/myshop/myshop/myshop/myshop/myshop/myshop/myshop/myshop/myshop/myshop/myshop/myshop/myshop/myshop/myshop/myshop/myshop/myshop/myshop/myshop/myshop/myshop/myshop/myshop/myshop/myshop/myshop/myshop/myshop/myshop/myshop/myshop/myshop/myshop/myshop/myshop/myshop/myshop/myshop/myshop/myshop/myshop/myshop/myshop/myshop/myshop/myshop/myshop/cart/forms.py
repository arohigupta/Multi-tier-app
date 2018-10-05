# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:34:53-07:00
# @Email:  agupta@juniper.net
# @Filename: forms.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T15:35:33-07:00

from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
