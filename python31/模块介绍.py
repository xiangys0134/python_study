#!/user/bin/env python3
# -*- coding: utf-8 -*-

import time,csv

ret = time.strftime('%Y-%m-%d %H:%M:%S')

print(ret)
aa  = time.localtime(15585445522)
print('aa',aa)
res = time.localtime()
print(res)
print(time.strftime('%Y-%m-%d %H:%M:%S',aa))