#!/usr/bin/env python
# -*- coding:utf-8 -*-


import hashlib

md5 = hashlib.md5()

md5.update(b"hello ")
md5.update(b"python")

print(md5.hexdigest())

