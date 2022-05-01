#!/user/bin/env python3
# -*- coding: utf-8 -*-
import struct

ret = struct.pack("i",111)

print(ret,len(ret))

res = struct.unpack("i",ret)

print(res[0])