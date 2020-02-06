#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import path,re_path
from django.shortcuts import render,redirect,HttpResponse
from  app01.models import *
from app02.models import *
from django.utils.safestring import mark_safe
from django.urls import reverse

class ModelStark():

    list_display_links = []
    def __init__(self,model):
        self.model = model
        self.model_name=self.model._meta.model_name
        self.app_label=self.model._meta.app_label
        self.app_model=(self.app_label,self.model_name)





    list_display=["__str__"]

    def _checkbox(self, obj=None, is_header=False):
        if is_header:
            return "选择"
        return mark_safe("<input type='checkbox''>")

    def edit(self, obj=None, is_header=False):
        if is_header:
            return "编辑"
        return mark_safe("<a href='%s'>编辑</a>" % self.get_change_url(obj))

    def _delete(self, obj=None, is_header=False):
        if is_header:
            return "删除"
        return mark_safe("<a href='%s'>删除</a>" % self.get_delete_url(obj))

    def show_authors(self, obj=None, is_header=False):
        if is_header:
            return "作者"
        # print(obj.authors.all())
        return " ".join([obj.name for obj in obj.authors.all()])

    def get_new_list_disply(self):
        new_list_disply = []
        new_list_disply.extend(self.list_display)
        new_list_disply.insert(0, ModelStark._checkbox)
        if not self.list_display_links:
            new_list_disply.append(ModelStark.edit)
        new_list_disply.append(ModelStark._delete)
        return new_list_disply


    def get_add_url(self):
        _url=reverse("%s_%s_add"%self.app_model)
        return _url

    def get_list_url(self):
        _url=reverse("%s_%s_list"%self.app_model)
        return _url

    def get_change_url(self,obj):
        _url=reverse("%s_%s_change"%self.app_model,args=(obj.pk,))
        return _url

    def get_delete_url(self,obj):
        _url=reverse("%s_%s_delete"%self.app_model,args=(obj.pk,))
        return _url

    def list_view(self,request):
        # x = self.x

        # 获取表头
        header_list = []
        for field in self.get_new_list_disply():
            try:
                field_obj = self.model._meta.get_field(field)
                header_list.append(field_obj.verbose_name)
            except Exception as e:
                if field == "__str__":
                    val = self.model._meta.model_name.upper()
                else:
                    val = field(self,is_header=True)
                header_list.append(val)

            # if callable(field):
            #     pass
            # else:
            #     field_obj = self.model._meta.get_field(field)
            #     header_list.append(field_obj.verbose_name)






        #展示当前表数据
        data = []
        queryset = self.model.objects.all()

        for obj in queryset:
            temp = []
            for field in self.get_new_list_disply():
                if callable(field):
                    file_data = field(self,obj)
                else:
                    file_data = getattr(obj,field)
                    if field in self.list_display_links:
                        file_data = "<a href='%s'>%s</a>"%(self.get_change_url(obj),file_data)
                temp.append(mark_safe(file_data))
            data.append(temp)
        # print(data)

        table_name = self.model._meta.verbose_name
        add_url = self.get_add_url()
        return render(request, 'stark/list_view.html', locals())

    def add_view(self,request):
        return HttpResponse("add_view")

    def change_view(self,request,id):
        return  HttpResponse('change_view')

    def delete_view(self,request,id):
        return HttpResponse('delete_view')

    def get_urls2(self):
        temp =[
            path('',self.list_view,name="%s_%s_list"%self.app_model),
            path('add/',self.add_view,name="%s_%s_add"%self.app_model),
            re_path('(\d+)/change/',self.change_view,name="%s_%s_change"%self.app_model),
            re_path('(\d+)/delete/',self.delete_view,name="%s_%s_delete"%self.app_model),
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