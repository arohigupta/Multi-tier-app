# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-01T15:35:10-07:00
# @Email:  agupta@juniper.net
# @Filename: urls.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-01T15:35:27-07:00

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]
