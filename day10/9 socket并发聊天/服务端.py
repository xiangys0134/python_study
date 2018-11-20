#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
from socket import *

server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8000))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg = conn.recv(1024)
            print(msg)
            conn.send(msg.upper())
        except Exception:
            break
        conn.close

if __name__ == '__main__':
    while True:
        conn,client_addr = server.accept()
        p = Process(target=talk,args=(conn,client_addr))
        p.daemon=True
        p.start()
