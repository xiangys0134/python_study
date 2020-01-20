#!/usr/bin/env python
# -*- coding:utf-8 -*-


# print("app01")


from stark.service.sites import site

from . import models

site.register(models.Book)
site.register(models.Publish)

# print(site.__list2)