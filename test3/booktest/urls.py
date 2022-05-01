"""test3 URL Configuration

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
    re_path(r'^index/', views.index),
    re_path(r'^aaa/', views.index),
    re_path(r'^login$', views.login),
    re_path(r'^login_check$', views.login_check),
    re_path(r'^test_ajax$', views.ajax_test),
    re_path(r'^ajax_handle$', views.ajax_handle),
    re_path(r'^login_ajax$', views.login_ajax),
    re_path(r'^login_ajax_check$', views.login_ajx_check),
    re_path(r'^set_cookie$', views.set_cookie),
    re_path(r'^get_cookie$', views.get_cookie),
    re_path(r'^set_session$', views.set_session),
    re_path(r'^get_session$', views.get_session),
    re_path(r'^clear_session$', views.clear_session),
]
