#!/usr/bin/env python
# -*- coding:utf-8 -*-

import struct

ret = struct.pack("i",456)

print(ret,type(ret),len(ret))

res = struct.unpack("i",ret)

print(res[0])