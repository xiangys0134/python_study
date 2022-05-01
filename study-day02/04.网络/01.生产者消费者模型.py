#!/user/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import threading
from queue import Queue as QUEUE
from queue import Empty

import os

ip_alive = []
ip_unreacheable = []
def is_reacheable(ip):
    sshport='31235'
    winport='3389'
    if os.path.exists('ip_alive.txt'):
        os.remove('ip_alive.txt')
    if os.path.exists('ip_unreacheable.txt'):
        os.remove('ip_unreacheable.txt')
    if not subprocess.call(["ping","-c","2","-w","2",ip]) or not subprocess.call(["nc","-v","-w","1",ip,"-z",sshport]) or not subprocess.call(["nc","-v","-w","1",ip,"-z",winport]):
        ip_alive.append(ip)
    else:
        ip_unreacheable.append(ip)


def is_queue(q):
    try:
        while True:
            ip = q.get_nowait()
            is_reacheable(ip)
    except Exception as e:
        pass

def main():
    q = QUEUE()
    for i in range(1,255):
        host_ip = "192.168.0.%s"%i
        q.put(host_ip)
    threads = []
    for i in range(10):
        thr = threading.Thread(target=is_queue,args=(q,))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()

    with open('ip_alive.txt', 'a+',encoding='utf-8') as f1, open('ip_unreacheable.txt', 'a+',encoding='utf-8') as f2:
        for ip in ip_alive:
            f1.write(ip)
            f1.write("\n")
        for ip in ip_unreacheable:
            f2.write(ip)
            f2.write("\n")

if __name__ == '__main__':
    main()


