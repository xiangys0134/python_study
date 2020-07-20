#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket


sock = socket.socket()

sock.connect(('127.0.0.1',8800))

sock.sendall('你好！'.encode('utf-8'))