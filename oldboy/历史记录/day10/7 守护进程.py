#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import time

class Myprocess(Process):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        print(os.getpid(),self.name)
        print('%s正和女主播聊天' %(self.name))

if __name__ == '__main__':
    p = Myprocess('alex')
    p.daemon=True
    p.start()
    time.sleep(10)
    print('主')