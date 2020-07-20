#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.contrib import admin
from django.urls import path,re_path
from app01 import views
from django.conf.urls import url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'aritcles/(?P<y>\d{4})/(?P<m>\d{2})/$',views.special_case_2003),
    re_path(r'index/$',views.index),
    re_path(r'login/',views.login),
]

