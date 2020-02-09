#!/user/bin/env python3
# -*- coding: utf-8 -*-

from stark.service.sites import site,ModelStark


from . models import *

class PermissionConfig(ModelStark):
    list_display = ["title","url"]

site.register(User)
site.register(Permission,PermissionConfig)
site.register(Role)