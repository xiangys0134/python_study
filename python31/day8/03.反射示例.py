#!/user/bin/env python3
# -*- coding: utf-8 -*-

import daniu

func = 'chi'
a = getattr(daniu,func)
# a()

s2 = 'person'
a = getattr(daniu,s2.capitalize())

print(a)