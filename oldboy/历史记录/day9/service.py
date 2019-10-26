#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import socket

phone = socket.socket()

phone.bind(('127.0.0.1',8000))
phone.listen(5)

print('start listen...')
conn,addr = phone.accept()
print(conn,addr)

msg = conn.recv(1024)
print('对方消息是:',msg)

msg_str = msg.decode('utf8')
print(type(msg_str))
answer = msg_str+'abc'
print(answer,type(answer),'####')
answer = answer.encode('utf8')
#answer = 'abc'.encode('utf8')

conn.send(answer)

conn.close()
phone.close()