#!/usr/bin/python
# -*- coding: utf-8 -*-
import  socket

server = socket.socket()
server.bind(('127.0.0.1',8003))
server.listen(4)
conn,addr = server.accept()
while True:
    msg = conn.recv(1024)
    msg = '%s sb'%(msg.decode('utf8'))
    conn.send(msg.encode())

conn.close()
server.close()


