#!/usr/bin/env python
# -*- coding:utf-8 -*-

#操作系统在控制时间


import time


# print(time.time())
#
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
#
# print(time.localtime())



#时间戳时间转格式化时间

# str_time = 1586223680.0246928
#
# print(time.localtime(str_time))
#
# ###结构化时间转换为格式化时间
#
# local_time = time.localtime(str_time)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S',local_time))

def func(m):
    str_time = time.strftime(m)

    struct_time = time.strptime(str_time + '-1','%Y-%m-%d')

    strf_time = time.mktime(struct_time)
    print(strf_time)


func('2020-4')












