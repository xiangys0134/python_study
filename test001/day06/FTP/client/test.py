#!/usr/bin/env python
# -*- coding:utf-8 -*-

head_info = {'action': 'put', 'filesize': 178708, 'filename': 'kubernetes.txt.pdf'}

print(type(head_info))
print(head_info.get('action'))

import os
filename = 'aaa'
res = os.path.join("putdir",filename)

print(res)