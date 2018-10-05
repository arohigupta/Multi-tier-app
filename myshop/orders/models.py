# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:44:43-07:00
# @Email:  agupta@juniper.net
# @Filename: models.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T16:41:14-07:00


from django.db import models
from shop.models import Product

# Create your models here.
'''
This model is used to diff between paid and unpaid orders
'''

class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

'''
stores amount and quantity paid for each item
'''
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
