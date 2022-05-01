#!/user/bin/env python3
# -*- coding: utf-8 -*-

import sys
#以下两种方法均可实现std功能

for line in sys.stdin:
    print(line,end='')


def get_content():
    return sys.stdin.readlines()

print(get_content())