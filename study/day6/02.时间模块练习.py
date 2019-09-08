#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
str_time = time.strftime('%Y-%m')
print(str_time)

struct_time = time.strptime(str_time+'-1','%Y-%m-%d')
print(struct_time)

mk_time = time.mktime(struct_time)

print(mk_time)