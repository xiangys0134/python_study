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
    path('admin/', admin.site.urls),
    re_path(r'index$', views.index),
    re_path(r'static_test$', views.static_test),
    re_path(r'index$', views.index),
    re_path(r'show_upload$', views.show_upload),
    re_path(r'upload_handle$', views.upload_handle),
    re_path(r'show_area/(?P<id>\d*)$', views.show_area),
    re_path(r'^areas$', views.areas),
    re_path(r'^prov$', views.prov),
    re_path(r'^city/(?P<id>\d+)$', views.city),
]