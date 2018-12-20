#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket

sk = socket.socket()
sk.bind(('127.0.0.1',8800))
sk.listen(5)

conn,addr = sk.accept()

ret = conn.recv(1024)
print(ret)

conn.send(b'hi')
conn.close()

sk.close()



