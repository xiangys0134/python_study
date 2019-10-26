from django.contrib import admin
from django.urls import path,include
from APP import views

urlpatterns = [
    path('index/', views.index),
    # path('addstudent/', views.addstudent),
    # path('getstudents/', views.getstudents),
    # path('deletestudent/', views.deletestudent),
    path('adduser/', views.adduser),
    path('getuser/', views.getuser),
    path('userupdate/', views.userupdate),
    path('deleteuser/', views.deleteuser),
]

