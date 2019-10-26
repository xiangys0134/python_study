#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import hashlib
import struct
import socket
import json

dir = os.path.dirname(os.path.abspath(__name__))

if not os.path.exists(os.path.join(dir,'ftpdata')):
    ftp_dir = os.path.join(dir,'ftpdata')
    os.mkdir(ftp_dir)
else:
    ftp_dir = os.path.join(dir, 'ftpdata')

service = socket.socket()
service.bind(('127.0.0.1',8000))
service.listen(5)

class Myserver:
    def __init__(self,sk):
        self.conn,self.addr = sk.accept()

    def mysend(self, msg):
        self.conn.send(msg)

    def myrecv(self, buffer=1024):
        return self.conn.recv(buffer)

    def stuck_unpack(self):
        msg = self.myrecv(4)
        print(msg)
        if not msg: return 'error'
        dic_byte = struct.unpack('i', msg)[0]
        print(dic_byte,'长度')
        byte_msg = self.myrecv(dic_byte)
        str_dic = byte_msg.decode('utf8')
        # dic = { 'filename':'filename','byte_size':byte_size,'md5':md5}
        str_msg = json.loads(str_dic)
        return str_msg
        # get_size = str_msg['name']['byte_size']

    def stuck_pack(self, dic):
        if not dic: return 'error'
        byte_dic = json.dumps(dic).encode('utf8')
        dic_pak = struct.pack(byte_dic)
        if hasattr(self, 'mysend'):
            func = getattr(self, 'mysend')
            func(dic_pak)


    def conn_close(self):
        self.conn.close()

if __name__ == '__main__':
    while True:
        sk = Myserver(service)
        while True:
            # try:
                #获取客户端字典
                msg_dic = sk.stuck_unpack()
                print(msg_dic,'################')
                data_recv = b''
                data_leng = 0
                m = hashlib.md5()
                with open(os.path.join(ftp_dir,msg_dic['filename']),'wb') as f:
                    while data_leng < msg_dic['file_size']:
                        if msg_dic['file_size'] < 1024:
                            data = sk.myrecv(msg_dic['file_size'])
                            data_leng += len(data)
                        else:
                            data = sk.myrecv(1024)
                            data_recv += data
                            data_leng += len(data)
                        f.write(data)
                        f.seek(data_leng)
                        print(data_leng,'&&&&&&')
                        m.update(data)
                    md5 = m.hexdigest()
                    print(md5)
                print('aaaa')
                #再次获取客户端字典
                new_dic = sk.stuck_unpack()
                print(new_dic)
                if md5 == new_dic['md5']:
                    print('md5',md5)
                else:
                    print('md5值不一致，上传失败')
            # except Exception:
            #     print('cccccccccc')
            #     sk.conn_close()
            #     break

    service.close()