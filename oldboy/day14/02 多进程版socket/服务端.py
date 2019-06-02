#!/usr/bin/env python
# -*- coding:utf-8 -*-
from  multiprocessing import Process
import socket



def talk(conn):
    while True:
        try:
            msg = conn.recv(1024)
            conn.send(msg.upper())
        except Exception:
            break
    conn.close()

if __name__ == '__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 8801))
    server.listen(3)
    while True:
        conn,addr = server.accept()
        p = Process(target=talk,args=(conn,))
        p.start()
    server.close()
