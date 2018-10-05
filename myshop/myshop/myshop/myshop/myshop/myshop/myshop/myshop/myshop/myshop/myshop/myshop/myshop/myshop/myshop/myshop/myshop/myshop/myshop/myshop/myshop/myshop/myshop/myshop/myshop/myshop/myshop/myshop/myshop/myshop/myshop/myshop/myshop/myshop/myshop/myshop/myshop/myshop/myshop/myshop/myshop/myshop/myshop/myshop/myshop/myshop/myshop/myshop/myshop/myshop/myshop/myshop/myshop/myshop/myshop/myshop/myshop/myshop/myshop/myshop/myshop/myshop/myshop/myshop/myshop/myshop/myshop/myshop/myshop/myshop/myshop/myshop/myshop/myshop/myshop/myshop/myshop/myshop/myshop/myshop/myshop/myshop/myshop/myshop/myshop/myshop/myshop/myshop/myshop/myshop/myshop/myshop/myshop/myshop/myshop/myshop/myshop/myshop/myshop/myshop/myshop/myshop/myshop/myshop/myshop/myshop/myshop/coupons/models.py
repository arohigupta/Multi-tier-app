# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T12:15:34-07:00
# @Email:  agupta@juniper.net
# @Filename: models.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T12:19:30-07:00

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
'''
code: Users enter this to apply to the order.
valid_from-valid_to: range for which the coupon is valid
discount: amount of discount for the code. This is a percentage. We use validators for this views.
active: Says if the coupon is active.
'''

class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
