# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T13:15:00-07:00
# @Email:  agupta@juniper.net
# @Filename: urls.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T13:15:03-07:00

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^apply/$', views.coupon_apply, name='apply'),
]
