#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,os

def main():
    print(sys.argv)

    print(sys.argv[1],sys.argv[2])

    if not os.access('/tmp/webtatic_repo.conf',os.X_OK):
        raise SystemExit('error')
    print('aaaaa')
if __name__ =='__main__':
    main()