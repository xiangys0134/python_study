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
from booktest import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index3/$', views.index,name='index2'),
    re_path(r'^index2/$', views.index2),
    re_path(r'^temp_var/$', views.temp_var),
    re_path(r'^temp_tags/$', views.temp_tags),
    re_path(r'^temp_filter/$', views.temp_filter),
    re_path(r'^temp_inherit/$', views.temp_inherit),
    re_path(r'^html_escape/$', views.html_escape),
    re_path(r'^change_pwd$', views.change_pwd),
    re_path(r'^login_check$', views.login_check),
    re_path(r'^login/$', views.login),
    re_path(r'^change_pwd_action$', views.change_pwd_action),
    re_path(r'^url_reverse$', views.url_reverse),
    re_path(r'^show_args/(\d+)/(\d+)$', views.show_args,name='show_args'),
    re_path(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$', views.show_kwargs,name='show_kwargs'),
    re_path(r'^test_redirect/$', views.test_redirect),
]
