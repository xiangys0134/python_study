#!/usr/bin/python
# -*- coding: utf-8 -*-

import multiprocessing
import threading
import os
import socket

s = socket.socket()
s.bind(('127.0.0.1',9000))
s.listen(5)

def action(conn):
    while True:
        data = conn.recv(1024)
        print(data)
        conn.send(data.upper())

if __name__ == '__main__':
    while True:
        conn,addr = s.accept()

        p = threading.Thread(target=action,args=(conn,))
        p.start()
