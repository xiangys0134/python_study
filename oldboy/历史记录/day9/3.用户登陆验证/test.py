#!/usr/bin/env python
# -*- coding:utf-8 -*-

# import struct
#
# a = b'dd'
#
# ret = struct.pack('i',len(a))
# print(ret,len(ret))
#
# ret_1 = struct.unpack('i',ret)[0]
# print(ret_1)

#
# import hashlib
#
# m = hashlib.md5()
# m.update('123'.encode('utf-8'))
# # m.update('in python hashlib'.encode('utf-8'))
# print(m.hexdigest())


# import json
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
# str_dic = json.dumps(dic)  #序列化：将一个字典转换成一个字符串
# print(type(str_dic),str_dic)  #<class 'str'> {"k3": "v3", "k1": "v1", "k2": "v2"}
#
# import os,sys
# db_dir = os.path.dirname(os.path.abspath(__name__))
# print(db_dir)
# import os,sys
#
# fsize = os.path.getsize(filePath)
# fsize = fsize/float(1024*1024)
# print(round(fsize,2))