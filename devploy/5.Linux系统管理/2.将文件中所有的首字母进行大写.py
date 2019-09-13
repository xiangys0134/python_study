#!/usr/bin/python
# -*- coding: utf-8 -*-
# 将文件中所有的首字母进行大写
import os

with open(os.path.join('/tmp','yum_save_tx.2019-09-03.16-40.xtYDie.yumtx')) as inf,open('/tmp/cc.txt','w') as outf:
     for line in inf:
         cmd = [item.capitalize() for item in line.split()]
         outf.write(' '.join(cmd))
         outf.write('\n')