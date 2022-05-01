#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django import template
register = template.Library()   #不可改变

@register.filter

def multi_fileter(x,y):
    return x * y