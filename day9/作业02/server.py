#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import hashlib
import struct
import socket
import json

class Myserver:
    def __init__(self,sk):
        self.conn,self.addr = sk.accept()

    def mysend(self, msg):
        self.sk.send(msg)

    def myrecv(self, buffer=1024):
        return self.sk.recv(buffer)

    def stuck_unpack(self):
        """"""
        msg = self.sk.myrecv(4)
        if not msg: return 'error'
        dic_byte = struct.unpack('i', msg)[0]
        byte_msg = msg.decode('utf8')
        # dic = { 'name1':{'filename':'filename','byte_size':byte_size,'md5':md5}}
        str_msg = json.loads(byte_msg)
        return str_msg
        # get_size = str_msg['name']['byte_size']

    def stuck_pack(self, dic):
        """
        dic = {
          'file_name1':{'filename':'filename','byte':byte_size,'md5':md5}
          'file_name2':{'filename':'filename','byte_size':byte_size,'md5':md5}
        }
        """
        if not dic: return 'error'
        byte_dic = json.dumps(dic).encode('utf8')
        dic_pak = struct.pack(byte_dic)
        if hasattr(self, 'mysend'):
            func = getattr(self, 'mysend')
            func(dic_pak)


    def conn_close(self):
        self.sk.close()