#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import hashlib
import struct
import socket
import json

# client = socket.socket()
# server_ip = ('127.0.0.1',8000)
class Myclient:
    def __init__(self):
        self.sk = socket.socket()
        self.sk.connect(('127.0.0.1',8000))

    def mysend(self,msg):
        self.sk.send(msg)

    def  myrecv(self,buffer=1024):
        return self.sk.recv(buffer)

    def stuck_unpack(self):
        msg = self.sk.myrecv(4)
        if not msg: return 'error'
        dic_byte = struct.unpack('i', msg)[0]
        byte_msg = self.sk.myrecv(dic_byte)
        str_dic = byte_msg.decode('utf8')
        # dic = { 'filename':'filename','byte_size':byte_size,'md5':md5}
        str_msg = json.loads(str_dic)
        return str_msg
        # get_size = str_msg['name']['byte_size']

    def stuck_pack(self,dic):
        if not dic:return 'error'
        print(dic)
        byte_dic = json.dumps(dic).encode('utf8')
        # print(byte_dic)
        dic_pak = struct.pack('i',len(byte_dic))
        print(dic_pak)
        if hasattr(self,'mysend'):
            # print('aaaa')
            func = getattr(self,'mysend')
            func(dic_pak)
            func(byte_dic)
        else:
            print('error')

    def conn_close(self):
        self.sk.close()

if __name__ == '__main__':
    client_socket = Myclient()
    dic = {}
    while True:
        tmp_dir = input(r'请输入上传路径：')
        if not tmp_dir:break
        if os.path.exists(tmp_dir):
            dic['filename'] = os.path.basename(tmp_dir)
            dic['file_size'] = os.path.getsize(tmp_dir)

        #将字典传给服务端
        client_socket.stuck_pack(dic)

        #开始传送数据
        m = hashlib.md5()
        with open(tmp_dir,'rb') as f:
            for line in f:
                client_socket.mysend(line)
                print(len(line),'&&&&')
                m.update(line)

        md5_id = m.hexdigest()
        print(md5_id)
        dic['md5'] = md5_id
        #再次将md5以字典的形式传给服务端
        client_socket.stuck_pack(dic)


    client_socket.conn_close()
        # def stuck_unpack(sk,msg)
    client_socket.conn_close()



