#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import reduce


ret = reduce(lambda x,y:x+y,range(101))
print(ret)


