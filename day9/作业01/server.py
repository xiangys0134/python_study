#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import struct


class My_socket:
    def __init__(self,conn):
        self.conn = conn

    def myrecv(self,buffer=1024):
        msg = self.conn.recv(buffer)
        return msg

    def mysend(self,msg):
        self.conn.send(msg)





