#!/user/bin/env python3
# -*- coding: utf-8 -*-

import importlib

from s1 import b

m1 = 'datetime'
ret = importlib.import_module(m1)

# print(ret)
# a = getattr(ret,'now')
#
# print(a())

# print(ret.datetime.now())

# b.bbb()

s1 = 's1.b'

ret  = importlib.import_module(s1)

print(ret.bbb())