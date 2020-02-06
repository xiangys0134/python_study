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

    # list_display = ["title", "publish","pub_date", "price",show_authors,edit,_delte]
    list_display = ["title", "publish","pub_date", "price"]
    list_display_link = ["title","price"]
    search_fields = ["title","price"]
    # def list_view(self, request):
    #     x = self.x
    #     queryset_obj = self.model.objects.all()
    #     return render(request, "stark/list.html", locals())




site.register(Book,BookConfig)
site.register(AuthorDetail)
site.register(Publish)
site.register(Author)

print(site._registry)