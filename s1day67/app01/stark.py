#!/user/bin/env python3
# -*- coding: utf-8 -*-

from stark.service.sites import site,ModelStark
from .models import *



site.register(Order)
site.register(Customer)