#!/usr/bin/env python
# -*- coding:utf-8 -*-

import daliu


func = input('输入：').strip()

ret = getattr(daliu,func)
f = hasattr(daliu,func)
print(ret())
print(f)
