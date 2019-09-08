#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
stu_time = time.time()-86400000 * 3

local_time = time.localtime(stu_time)

print(local_time)