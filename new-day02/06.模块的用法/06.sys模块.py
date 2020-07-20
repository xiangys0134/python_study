#!/usr/bin/env python
# -*- coding:utf-8 -*-


import sys


def foo(*args):
    print(args)
    sys.exit(5)
    # print('aaaa')


if __name__ == '__main__':
    print(sys.argv)
    foo(*sys.argv[1:])

