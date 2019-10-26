#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Two import views

from django.contrib import admin
from django.urls import path
from Two import views

urlpatterns = [
    path('index/', views.index),
]