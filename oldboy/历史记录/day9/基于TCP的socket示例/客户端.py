#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

client = socket.socket()
client.connect(('127.0.0.1',8080))
client.send('aab'.encode('utf8'))
client.close()