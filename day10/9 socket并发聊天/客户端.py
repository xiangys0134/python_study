#!/usr/bin/python
# -*- coding: utf-8 -*-
from socket import *

client = socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8000))

while True:
    msg = input('>>：').strip()
    client.send(msg.encode('utf8'))
    print('-' * 120)
    rev_msg = client.recv(1024)
    print(rev_msg)