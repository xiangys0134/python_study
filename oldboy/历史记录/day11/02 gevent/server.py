#!/usr/bin/python
# -*- coding: utf-8 -*-

from gevent import  monkey
monkey.patch_all()
from  socket import *
import gevent

def server(server_ip,port):
    s = socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR)
    s.bind(5)
    while True:
        conn,add = s.accept()
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    try:
        while True:
            res = conn.recv(1024)
            print('client ')
