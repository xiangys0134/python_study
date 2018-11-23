# -*- coding: utf-8 -*-
# @Time    : 2018/11/11 0011 18:14
# @Author  : Luffy
# @Email   : customer@luffycity.com
# @File    : json模块的使用.py
# @Software: PyCharm

import json

data = {
    "file_name": "xx.avi",
    "file_size": 1024 * 1024 * 1024,
    "MD5": "wqe121313131wqs"
}


ret = json.dumps(data)
print(ret, type(ret))
