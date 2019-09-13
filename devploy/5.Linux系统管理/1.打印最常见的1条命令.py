#!/usr/bin/python
# -*- coding: utf-8 -*-
# 统计使用最常见的10条历史命令
import os
from collections import Counter

c = Counter()
with open(os.path.expanduser('~/.bash_history')) as f:
    for line in f:
        cmd = line.strip().split()
        if cmd:
            c[cmd[0]] += 1
print(c)
