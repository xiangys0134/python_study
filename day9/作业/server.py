#!/usr/bin/python
# -*- coding: utf-8 -*-

from multiprocessing import Process
import os
import socket
import time
import os

server = socket.socket()
server.bind(('127.0.0.1',8000))
server.listen(5)


class Myserver:
    def __init__(self,server):
        self.conn,self.addr = server.accept()


    def myrecv(self):
        msg = self.conn.recv(1024)
        # print(msg.decode('utf8'))
        return msg.upper()

    def mysend(self,msg):
        self.conn.send(msg.encode('utf8'))


while True:
    a = Myserver(server)
    msg = a.myrecv()
    print(msg)

