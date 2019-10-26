#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket

client =socket.socket
client.connect(('127.0.0.1',9000))
client.send()