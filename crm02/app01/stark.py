#!/user/bin/env python3
# -*- coding: utf-8 -*-

print("app01...")

from stark.service.sites import site,ModelStark
from . models import AuthorDetail,Book,Publish,Author
from django.shortcuts import HttpResponse,render,redirect
from django.utils.safestring import mark_safe

class BookConfig(ModelStark):
    x = 20



    #展示表头数据
    # header_list = ["名称","出版社","出版时间","价格"]

    def show_authors(self,obj=None,is_head=False):
        if is_head:
            return "作者"
        return " ".join([obj.name for obj in obj.authors.all() ])

    # list_display = ["title", "publish","pub_date", "price",show_authors,edit,_delte]
    list_display = ["title", "publish","pub_date", "price",show_authors]
    list_display_link = ["title","price"]
    search_fields = ["title","price"]
    list_filter = ["publish","authors"]
    # def list_view(self, request):
    #     x = self.x
    #     queryset_obj = self.model.objects.all()
    #     return render(request, "stark/list.html", locals())

    def patch_init(self,request,queryset):
        queryset.update(price=100)

    patch_init.short_desc="批量初始化"
    actions = [patch_init]


class AuthorConfig(ModelStark):
    # def show_gender(self,obj=None,is_head=False):
    #     if is_head:
    #         return "性别"
    #     return obj.get_gender_display()
    list_display = ["name","age","gender"]
    list_filter = ["gender"]

site.register(Book,BookConfig)
site.register(AuthorDetail)
site.register(Publish)
site.register(Author,AuthorConfig)

print(site._registry)
