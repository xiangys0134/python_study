#!/usr/bin/env python
# -*- coding:utf-8 -*-

import hashlib

md5 = hashlib.md5()

md5.update(b"hello")
md5.update(b" yuan!")
print(md5.hexdigest())  #600b4b15923c0f39a5925d27eb932e2d

