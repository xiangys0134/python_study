#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
a = time.strftime("%H:%M:%S",time.localtime())
# print(a,type(a))

send_time = "19:12:40"
while True:
    a = time.strftime("%H:%M:%S", time.localtime())
    if a == send_time:
        print('sssssssssssss')
        time.sleep(2)
    else:
        #time.sleep(1)
        pass
        break