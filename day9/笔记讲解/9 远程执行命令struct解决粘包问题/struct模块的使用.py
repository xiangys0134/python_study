# -*- coding: utf-8 -*-
"""
struct能把数据转换成固定长度的bytes
"""

import struct

total_size = 10240

ret = struct.pack('i', total_size)
print(ret, len(ret))

# 解包
ret2 = struct.unpack('i', ret)
print(ret2[0])
