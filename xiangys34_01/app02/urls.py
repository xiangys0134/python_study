#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.contrib import admin
from django.urls import path,re_path,include
from app02 import views

urlpatterns = [
    re_path(r'^index/(\d{4})/$',views.index),
    # re_path(r'^order/(?P<year>\d{4})/(?P<month>\d{2})/$',views.order),
]
