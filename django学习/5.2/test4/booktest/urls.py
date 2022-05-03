"""test4 URL Configuration

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
from django.urls import path,re_path

from booktest import views,views1
urlpatterns = [
    re_path('^index/', views.index,name='index'),
    re_path('^temp_var/', views1.temp_var),
    re_path('^temp_tags/', views1.temp_tags),
    re_path('^temp_filter/', views1.temp_filter),
    re_path('^temp_inherit/', views1.temp_inherit),
    re_path('^login/', views.login),   #显示登陆界面
    re_path('^login_check$', views.login_check), #登陆验证
    re_path('^change_pwd$', views.change_pwd),  #修改密码页面
    re_path('^change_pwd_action$', views.change_pwd_action),  #修改密码页面
    re_path('^verify_code$', views.verify_code),  #产生验证码图片
    re_path('^url_reverse$', views.url_reverse),  #产生验证码图片
    re_path('^show_args/(\d+)/(\d+)', views.show_args,name='show_args'),  #产生验证码图片
    re_path('^show_kwargs/(?P<c>\d+)/(?P<d>\d+)', views.show_kwargs,name='show_kwargs'),  #产生验证码图片
    re_path('^test_redirect$', views.test_redirect,name='test_redirect'),  #产生验证码图片
]
