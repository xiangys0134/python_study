#!/user/bin/env python3
# -*- coding: utf-8 -*-

from django.template import Library

# 创建一个Library类的对象

register = Library()

@register.filter
def mod(num):
    '''判断num是否为偶数'''
    return num%2  == 0

@register.filter
def mod_val(num,val):
    '''判断num是否能被val正常'''
    return num%val == 0