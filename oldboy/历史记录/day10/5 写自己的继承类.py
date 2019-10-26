#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
import time

class MyProcess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(os.getpid())
        print('%s 正在和女主播聊天' %(self.name))


if __name__ == '__main__':

    p1 = MyProcess('wupeiqi')
    #
    p1.start()
    print('主线程')
