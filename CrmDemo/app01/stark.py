#!/usr/bin/env python
# -*- coding:utf-8 -*-

print("app01...")

from stark.service.sites import site,ModelStark
from . models import Book,Publish,Author,AuthorDetail


class BookConfig(ModelStark):
    pass

site.register(Book,BookConfig)
site.register(Author)
site.register(AuthorDetail)
site.register(Publish)

print(site._registry)


