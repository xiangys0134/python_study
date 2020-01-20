#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path,re_path
from django.shortcuts import render,redirect,HttpResponse

from app01.models import *
from app01.models import *


class ModelStark(object):
    x = 100

    def __init__(self,model):
        self.model = model

    def list_view(self,request):
        query_set = Author.objects.all()

        x = self.x
        # print(query_set)
        return render(request,"list_view.html",locals())

    def add_view(self,request):
        return HttpResponse("add_view...")

    def change_view(self,request,id):
        return HttpResponse("change_view...")

    def delete_view(self,request,id):
        return HttpResponse("delete_view...")

    def get_urls(self):
        temp=[
            path('',self.list_view),
            path('add/',self.add_view),
            re_path('(\d+)/change/',self.change_view),
            re_path('(\d+)/delete/',self.delete_view),
        ]
        return temp

    @property
    def urls(self):
        return self.get_urls(),None,None

class StarkSite(object):
    def __init__(self):
        self._registry = {}



    def register(self,model,admin_class=None):
        admin_class = admin_class or ModelStark
        self._registry[model] = admin_class(model)

    def get_urls(self):
        temp = []

        for model,config_obj in self._registry.items():
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            temp.append(
                path('%s/%s/'%(app_label,model_name),config_obj.urls),       #{Book:BooConfig}
            )
            print('>>>>>>%s/%s'%(app_label,model_name))
            '''
            path('app01/book/',BookConfig(Book).urls),
            path('app01/book/',BookConfig(Book).list_view),
            path('app01/book/',BookConfig(Book).add_view),
            path('app01/book/',BookConfig(Book).change_view),
            path('app01/book/',BookConfig(Book).delete_view),
            
            
            
            path('app01/publish/',ModelStark(Book).urls),
            
            path('app01/publish/',ModelStark(Book).list_view),
            path('app01/publish/',ModelStark(Book).add_view),
            path('app01/publish/',ModelStark(Book).change_view),
            path('app01/publish/',ModelStark(Book).delete_view),
            
            '''
        return temp

    @property
    def urls(self):
        return self.get_urls(),None,None

site = StarkSite()






