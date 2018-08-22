#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid,socket
def get_mac_address():
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0,11,2)])

#a = get_mac_address
#print a()

#获取本机电脑名
myname = socket.getfqdn(socket.gethostname())
#获取本机ip
myaddr = socket.gethostbyname(myname)
print myname
print myaddr

l1 = []
l1.append()