# @Author: Arohi Gupta <agupta>
# @Date:   2018-10-02T10:16:15-07:00
# @Email:  agupta@juniper.net
# @Filename: celery.py
# @Last modified by:   agupta
# @Last modified time: 2018-10-02T10:16:24-07:00

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
