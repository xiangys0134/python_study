#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('app01...')

from  stark.service.sites import site,ModelStark
from . models import Book,Publish,Author,AuthorDetail
from django.utils.safestring import mark_safe

class BookConfig(ModelStark):
    x = 10000

    list_display_links = ["title"]
    # def _checkbox(self,obj=None,is_header=False):
    #     if is_header:
    #         return "选择"
    #     return mark_safe("<input type='checkbox''>")
    #
    # def edit(self,obj=None,is_header=False):
    #     if is_header:
    #         return "编辑"
    #     return mark_safe("<a href='/stark/app01/book/%s/change/'>编辑</a>"%obj.pk)
    #
    # def _delete(self,obj=None,is_header=False):
    #     if is_header:
    #         return "删除"
    #     return mark_safe("<a href='/stark/app01/book/%s/delete/'>删除</a>"%obj.pk)
    #
    # def show_authors(self,obj=None,is_header=False):
    #     if is_header:
    #         return "作者"
    #     # print(obj.authors.all())
    #     return " ".join([obj.name for obj in obj.authors.all()])
    list_display = ["title","price","pub_date","publish"]


class PublishConfig(ModelStark):
    x = 10

site.register(Book,BookConfig)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)


print(site._registry)

