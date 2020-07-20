#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# list1 = os.system("dir")
#
# print(list1)


ret = os.popen("ipconfig")

# print(ret.read())


# abs_path = os.path.abspath(__file__)
#
# dir_name = os.path.dirname(abs_path)
#
# print(os.path.join(dir_name,'hehe'))
#
# ret = os.path.sep
#
# print(ret)

ret = os.path.split(r'E:\python_study\new-day02\06.模块的用法\02.模块的基本使用.py')

print(ret)
print(os.path.exists(r'E:\python_study\new-day02\06.模块的用法\02.模块的基本使用.py'))