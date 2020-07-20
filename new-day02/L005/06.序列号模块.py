#!/usr/bin/env python
# -*- coding:utf-8 -*-

#为什么有序列号

import json

dic = {'key1':'value','key2':'value2'}

ret = json.dumps(dic)

print(ret,type(ret))

