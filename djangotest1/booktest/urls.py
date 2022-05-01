
from django.conf.urls import url
from django.urls import path,re_path,include

from booktest.views import *

urlpatterns = [
    #通过url函数设置url路由配置项
    path('index/',index),
    url('^books$',show_books),
    url(r'^books/(\d+)$',detail),
]