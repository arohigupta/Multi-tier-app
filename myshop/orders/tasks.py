# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T10:15:44-07:00
# @Email:  agupta@juniper.net
# @Filename: tasks.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T11:56:14-07:00

from celery import task
from django.conf import settings
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order. Your order id is {}.'.format(order.first_name,
                                                                             order.id)
    mail_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [order.email])
    return mail_sent
