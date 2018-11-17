#!/usr/bin/env python
# -*- coding:utf-8 -*-

import struct

a = b'dd'

ret = struct.pack('i',len(a))
print(ret,len(ret))

ret_1 = struct.unpack('i',ret)[0]
print(ret_1)