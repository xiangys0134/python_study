#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import time
import os
import random

class Myprocess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print('%s正在和网红脸聊天' %(self.name))
        time.sleep(random.randrange(1,5))
        print('%s还在和网红脸蛋聊天' %(self.name))

p1 = Myprocess('alex')
p1.start()

p1.terminate()  #关闭进程，不会立即关闭
print(p1.is_alive())

print('开始')
time.sleep(10)
print(p1.is_alive())
