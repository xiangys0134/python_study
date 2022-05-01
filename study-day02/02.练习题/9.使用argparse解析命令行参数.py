#!/user/bin/env python3
# -*- coding: utf-8 -*-


import argparse

def _argparse():
    parser = argparse.ArgumentParser(description="This is descirption")
    parser.add_argument('--host',action='store',dest='server',default='localhost',help='connect to host')
    parser.add_argument('-t',action='store_true',default=False,dest='boolean_switch',help='Set a switch to true')
    return parser.parse_args()

def main():
    parser = _argparse()
    print(parser)
    print('host=',parser.server)
    print('boolean_switch=',parser.boolean_switch)

if __name__ == '__main__':
    main()

'''
执行结果
[root@xiangys0134 tmp]# python3 parse.py --host=127.0.0.1 -t
Namespace(boolean_switch=True, server='127.0.0.1')
host= 127.0.0.1
boolean_switch= True
'''