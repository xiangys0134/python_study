#!/user/bin/env python3
# -*- coding: utf-8 -*-
#适用与小范围的多线程端口扫描，测试失败，不可以通过next()函数去取迭代值

import threading
from queue import Queue
from socket import *
import os
from itertools import product

ip_alive = []
ip_unreacheable = []

def conn_connect(ite_host):
    conn = socket(AF_INET,SOCK_STREAM)
    while True:
        try:
            host_port = next(ite_host)
            try:

                conn.connect(host_port)
                print('aviable',host_port)
                ip_alive.append(host_port)
                # print(host,port,'is availeable')
            except Exception as e:
                print('unreacheable', host_port)
                ip_unreacheable.append(host_port)
                # print(host_port,'is unavaileable')
                pass
            finally:
                conn.close()
        except Exception as e:
            break
def main():
    # host = "47.96.149.11"
    l1 = ["47.96.149.11","47.96.159.11"]
    l2 = range(20,23)
    host_port = product(l1,l2)


    theads = []
    conn_connect(host_port)
    # for i in range(0,25):
    #     conn_connect(host_port)
        # thr = threading.Thread(target=conn_connect,args=(host_port))
        # thr.start()
        # theads.append(thr)
    #
    # for thr in theads:
    #     thr.join()

    # print(ip_alive)
    if os.path.exists('ip_alive_sockert.txt'):
        os.remove('ip_alive_sockert.txt')

    if os.path.exists('ip_unreacheable_socket.txt'):
        os.remove('ip_unreacheable_socket.txt')
    with open('ip_alive_sockert.txt', 'a+',encoding='utf-8') as f1, open('ip_unreacheable_socket.txt', 'a+',encoding='utf-8') as f2:
        for ip,port in ip_alive:
            f1.write(str(ip)+' '+ str(port))
            f1.write("\n")
        for ip,port in ip_unreacheable:
            f2.write(str(ip)+' '+ str(port))
            f2.write("\n")


if __name__ == '__main__':
    main()