#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django.urls import path,re_path
from django.shortcuts import HttpResponse,redirect,render
from app01.models import Book
from django.utils.safestring import mark_safe
from django.urls import reverse
from django import forms
from stark.utils.page import Pagination

class ShowList():
    def __init__(self,config_obj,request,queryset_obj):
        self.config_obj = config_obj
        self.request = request
        self.queryset_obj = queryset_obj
        # self.pagination = self.getPagination()
        self.get_search_queryset()
        self.getPagination()


    def get_search_queryset(self):
        val = self.request.GET.get("q")
        if val:
            print(self.config_obj.search_fields)
            self.search_default_val = val
            from django.db.models import Q
            search_condition = Q()
            search_condition.connector = "or"
            for search_field in self.config_obj.search_fields:
                search_condition.children.append((search_field + "__icontains",val))
                # search_condition.children.append((search_field + "__icontains", val))


            self.search_queryset = self.queryset_obj.filter(search_condition)
            self.queryset_obj = self.search_queryset
            # print("queryset:",self.search_queryset)
        # print("queryset:",self.queryset_obj)
        #
        # return self.queryset_obj


    def getPagination(self):
        current_page = self.request.GET.get("page")
        if not current_page:
            current_page = 1
        print("&&&&&&&",self.request)
        print("*******",current_page)
        self.pagination = Pagination(current_page, self.queryset_obj.count(), self.request, per_page=3)
        self.pager_queryset = self.queryset_obj[self.pagination.start:self.pagination.end]

    def getPage_list(self):
        return self.pager_queryset.page_html_list()


    def show_header(self):
        # 构建表头数据
        header_list = []

        for field in self.config_obj.get_new_list_display():
            try:
                field_obj = self.config_obj.model._meta.get_field(field)
                header_list.append(getattr(field_obj, 'verbose_name'))
            except Exception as e:
                if field == "__str__":
                    val = self.config_obj.model._meta.model_name.upper()
                else:
                    val = field(self.config_obj, is_head=True)
                header_list.append(val)
        return header_list

    def show_body(self):
        # 构建表数据
        data = []
        # if self.search_queryset:
        #     self.pager_queryset =
        for obj in self.pager_queryset:
            temp = []
            for field in self.config_obj.get_new_list_display():
                if callable(field):
                    val = field(self.config_obj, obj)
                    print(val)
                else:
                    val = getattr(obj, field)
                    if field in self.config_obj.list_display_link:
                        val = mark_safe("<a href='%s'>%s</a>" % (self.config_obj.get_change_url(obj), val))
                temp.append(val)

            data.append(temp)
        return data

class ModelStark(): #配置类
    def __init__(self,model):
        self.model = model
        self.model_name = model._meta.model_name
        self.app_label = model._meta.app_label


    x = 100
    list_display = ["__str__"]
    list_display_link = []
    search_fields = []
    model_form_class=None

    def _checkbox(self,obj=None,is_head=False):
        if is_head:
            return "选择"
        return mark_safe("<input type='checkbox'>")

    def edit(self,obj=None,is_head=False):
        if is_head:
            return "编辑"
        _url = reverse("%s_%s_change"%(self.app_label,self.model_name),args=(obj.pk,))
        # return mark_safe("<a href='/stark/app01/%s/%s/change/'>编辑</a>"%(obj._meta.model_name,obj.pk))
        return mark_safe("<a href='%s'>编辑</a>"%(self.get_change_url(obj)))

    def _delte(self,obj=None,is_head=False):
        if is_head:
            return "删除"
        _delete = reverse("%s_%s_delete"%(self.app_label,self.model_name),args=(obj.pk,))
        return mark_safe("<a href='%s'>删除</a>"%(self.get_delete_url(obj)))

    def show_authors(self,obj=None,is_head=False):
        if is_head:
            return "作者"
        val = obj.authors.all()
        return " ".join([obj.name for obj in val])


    def get_new_list_display(self):
        new_list_display = []
        new_list_display.extend(self.list_display)
        new_list_display.insert(0,ModelStark._checkbox)
        if not self.list_display_link:
            new_list_display.append(ModelStark.edit)
        new_list_display.append(ModelStark._delte)

        return new_list_display


    #反向解析URL
    def get_change_url(self,obj):
        _url = reverse("%s_%s_change" % (self.app_label, self.model_name), args=(obj.pk,))
        return _url

    def get_add_url(self):
        _url = reverse("%s_%s_add" % (self.app_label, self.model_name))
        return _url

    def get_delete_url(self,obj):
        _url = reverse("%s_%s_delete" % (self.app_label, self.model_name), args=(obj.pk,))
        return _url

    def get_list_url(self):
        _url = reverse("%s_%s" % (self.app_label, self.model_name))
        return _url

    def list_view(self,request):
        x = self.x

        # print(self.list_display)
        # print(">>>",data)

        queryset_obj = self.model.objects.all()

        show_list = ShowList(self,request,queryset_obj)
        # data = show_list.show_body()
        # header_list = show_list.show_header()

        add_url = self.get_add_url()
        table_name = self.model._meta.verbose_name

        return render(request, "stark/list.html", locals())


    def get_model_form_class(self):
            from django import forms
            class BaseModelForm(forms.ModelForm):
                class Meta:
                    model = self.model
                    fields = "__all__"
            return self.model_form_class or BaseModelForm

    def add_view(self,request):
        # return HttpResponse("add_view....")

        DetailModeForm = self.get_model_form_class()

        if request.method =="GET":
            form = DetailModeForm
            return render(request,"stark/add_view.html",locals())
        else:
            form = DetailModeForm(request.POST)
            if form.is_valid():
                form.save()
                print(">>>>",self.get_list_url())
                return redirect(self.get_list_url())
            else:
                return render(request,"stark/add_view.html",locals())


    def change_view(self,request,id):
        edit_val = self.model.objects.filter(pk=id).first()
        DetailModeForm = self.get_model_form_class()
        if request.method == "GET":
            form = DetailModeForm(instance=edit_val)
            return render(request,"stark/change_view.html",locals())
        else:
            form = DetailModeForm(request.POST,instance=edit_val)
            if form.is_valid():
                form.save()
                return redirect(self.get_list_url())
            else:
                return render(request, "stark/change_view.html", locals())

    def delete_view(self,request,id):
        _del_val = self.model.objects.filter(pk=id).first()
        DetailModeForm = self.get_model_form_class()
        del_url = self.get_list_url()
        if request.method == "GET":
            form = DetailModeForm(instance=_del_val)
            return render(request,"stark/delete_view.html",locals())
        else:
            if request.POST["_delete"]:
                self.model.objects.filter(pk=id).delete()
        return redirect(self.get_list_url())

    @property
    def get_urls2(self):
        temp = [
            path("",self.list_view,name="%s_%s"%(self.app_label,self.model_name)),
            path("add/",self.add_view,name="%s_%s_add"%(self.app_label,self.model_name)),
            re_path("(\d+)/change/",self.change_view,name="%s_%s_change"%(self.app_label,self.model_name)),
            re_path("(\d+)/delete/",self.delete_view,name="%s_%s_delete"%(self.app_label,self.model_name)),
        ]

        return temp


class StarkSite():
    def __init__(self):
        self._registry = {}

    def register(self,model_or_iterable,admin_class=None):
        admin_class = admin_class or ModelStark
        self._registry[model_or_iterable] = admin_class(model_or_iterable)

    def get_urls(self):
        temp = []
        for model,config_obj in self._registry.items():
            model_name = model._meta.model_name
            app_label = model._meta.app_label
            temp.append(
                path('%s/%s/'%(app_label,model_name),(config_obj.get_urls2,None,None))
            )
        return temp

    @property
    def urls(self):
        return self.get_urls(),None,None

site = StarkSite()