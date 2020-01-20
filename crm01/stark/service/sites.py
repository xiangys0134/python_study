#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path,re_path
from django.shortcuts import render,redirect,HttpResponse
from  app01.models import *
from app02.models import *

class ModelStark():
    def __init__(self,model):
        self.model = model

    def list_view(self,request):
        x = 100
        queryset = Book.objects.all()
        return render(request,'list_view.html',locals())

    def add_view(self,request):
        return HttpResponse("add_view")

    def change_view(self,request,id):
        return  HttpResponse('change_view')

    def delete_view(self,request,id):
        return HttpResponse('delete_view')

    def get_urls2(self):
        temp =[
            path('',self.list_view),
            path('add/',self.add_view),
            re_path('(\d+)/change/',self.change_view),
            re_path('(\d+)/delete/',self.delete_view),
        ]

        return temp

    @property
    def urls2(self):
        return self.get_urls2(),None,None

class StarkSite():
    def __init__(self):
        self._registry = {}

    def get_urls(self):
        tmp =[]
        for model,config_obj in self._registry.items(): #{Booku:BookConfig(Booku),Publish:ModelStark(Publish)}
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            tmp.append(
                path('%s/%s/'%(app_label,model_name),config_obj.urls2),
            )

        return tmp
    @property
    def urls(self):
        return self.get_urls(),None,None

    def register(self,model,admin_class=None):
        admin_class = admin_class or ModelStark
        self._registry[model] = admin_class(model)





site = StarkSite()