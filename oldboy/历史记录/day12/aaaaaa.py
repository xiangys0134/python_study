#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

file_log = r'C:\bat_logs'

if os.path.exists(file_log):
    print('aaaa')
    # os.system(os.makedirs(file_log) )
else:
    print('not')