#!/usr/bin/env python
# -*- coding:utf-8 -*-

print('app02...')



from stark.service.sites import site
from . import models

site.register(models.Article)

print(site._registry)

