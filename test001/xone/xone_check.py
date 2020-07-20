#!/usr/bin/env python
# -*- coding:utf-8 -*-
# yousong.xiang
# 2020.5.27
# v1.0.1
# xone端口检查脚本,需要安装nc组件 yum install -y nc

import subprocess
import threading
import os
import logging


port_alive = []
port_unreacheable = []
port_list=[ 9761,
            9762,
            9763,
            9781,
            9766,
            9767,
            9768,
            9769,
            9770,
            9771,
            9999,
            8001,
            8032,
            8031,
            8061,
            8062,
            8063,
            8073,
            8852,
            8850,
            8851,
            8853,
            8860,
]


def is_reacheable(host_server,logger1,logger2):
    try:
        while port_list:
            port = port_list.pop()
            # print('port:',len(port_list))
            if not subprocess.call("nc -v -w 4 {} -z {}".format(host_server, port), shell=True):
                # print('seccuss：', port)
                port_alive.append(port)
                logger1.info('端口:{} 正常'.format(port))
            else:
                # print('fial：', port)
                port_unreacheable.append(port)
                logger2.error('端口:{} 异常'.format(port))
    except Exception as f:
        pass


def main():
    ab_path = os.path.abspath('./')
    res_log = os.path.join(ab_path, 'xone_status.log')
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=res_log,
                        filemode='a+')
    # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    logger1 = logging.getLogger('myapp.area1')
    logger2 = logging.getLogger('myapp.area2')

    threads = []
    # print(port_list)
    host_server = 'localhost'
    for i in range(1,10):
        thr = threading.Thread(target=is_reacheable,args=(host_server,logger1,logger2))
        thr.start()
        threads.append(thr)
    for thr in threads:
        thr.join()

    # print('ipalive:',port_alive)
    # print('ip_unreacheable:',port_unreacheable)

    if port_unreacheable:
        # print('存在异常端口')
        exit(4)


if __name__ == '__main__':
    main()