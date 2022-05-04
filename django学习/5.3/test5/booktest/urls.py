"""test5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from booktest import views

urlpatterns = [
    re_path('^index$', views.index),
    re_path('^static_test$', views.static_test),
    re_path('^show_upload$', views.show_upload),
    re_path('^upload_handle$', views.upload_handle),
    re_path('^show_area/(?P<pindex>\d*)$', views.show_area),
    re_path('^areas$', views.areas),
    re_path('^prov$', views.prov),
    re_path('^city/(\d+)$', views.city),
    re_path('^dis/(\d+)$', views.dis),
]
