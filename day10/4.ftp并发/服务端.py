#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import socket
from multiprocessing import Process



def talk(conn):
    while True:
        msg = conn.recv(1024)
        conn.send(msg.decode().upper().encode())
    conn.close

if __name__ == '__main__':
    server = socket.socket()
    server.bind(('127.0.0.1', 8001))
    server.listen(4)

    while True:
        conn,addr = server.accept()
        p1 = Process(target=talk,args=(conn,))
        # p1.daemon
        p1.start()
        # p1.join()

    server.close

