#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

import os

# ret = os.popen("dir")
#
# print(ret.read())


res = subprocess.Popen(
    "dir",
    shell=True,
    stderr=subprocess.PIPE,
    stdout=subprocess.PIPE,
)

print(res.stdout.read().decode("gbk"))
