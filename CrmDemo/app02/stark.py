#!/usr/bin/env python
# -*- coding:utf-8 -*-

from stark.service.sites import site,ModelStark
from . models import Article
# print("app02...")

site.register(Article)

print(site._registry)


