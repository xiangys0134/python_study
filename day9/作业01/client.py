#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import struct
import os

dic = {}

sk = socket.socket()
sk.connect(('127.0.0.1',8000))

class Myclient:
    def __init__(self,sk):
        self.

        pass

    def myrecv(self,buffer=1024):
        msg =