#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time

# print(time.time())

# s_t = time.strptime('2018.8.8',"%Y.%m.%d")
# print(s_t)
#
# mdtime = time.mktime(s_t)
#
# print(mdtime)

str_time = time.strftime('%Y-%m')

str = time.strptime(str_time+'-1','%Y-%m-%d')

print(time.mktime(str))