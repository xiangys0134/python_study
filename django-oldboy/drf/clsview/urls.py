"""drf URL Configuration

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
from clsview import views
from booktest.views import BookInfoAPIView,HeroInfoAPIView
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # 函数视图
    re_path(r'books/',views.get_books),

    # 类视图的路由
    re_path(r'book2/',views.BookInfoView.as_view())

]
