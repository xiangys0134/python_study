#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib,json,os,sys,subprocess,struct,socket

users_db = {
    'alex':'202cb962ac59075b964b07152d234b70',
    'gold':'202cb962ac59075b964b07152d234b70',
    'zhangsan':'202cb962ac59075b964b07152d234b70'
}

ftp_dir = os.path.dirname(os.path.abspath(__name__))
str_users = json.dumps(users_db)
print(str_users,type(str_users))
if os.path.exists('db'):
    with open(os.path.join('db','user_db'),'w',encoding='utf8') as f:
        f.write(str_users)

class Login_in:
    def __init__(self,user,password):
        self.user = user
        self.pasword = password

    def read(self):
        ftp_dirs = os.path.join(ftp_dir,'ftpdata')
        if os.path.exists(os.path.join(ftp_dirs,str(self.user))):
            obj = subprocess.Popen(
                "dir %s"%(os.path.join(ftp_dirs,str(self.user))),
                shell=True,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()
            ret = stdout if stdout else stderr
            print('文件夹：%s \n%s'%(self.user,ret.decode('gbk')))

    def upload(self,upload_file):
        # server = socket.socket()
        # server.bind(('127.0.0.1',8000))
        # server.listen(5)
        # while True:
        #     conn,addr = server.accept()
        #     while True:
        #         msg = conn.recv(1024)

        print('我上传了一个文件:%s'%(upload_file))

    def delete(self,file):
        print('我删除了一个文件%s'%(file))

    def shell(self,command):
        print('我执行了一个shell命令'%(command))

"""
alex:123
gold:123
zhangsan:123
"""
# username = input('请输入你的用户名：').strip()
# password = input('请输入你的密码：').strip()

username = 'alex'
password = '123'

#获取到用户alex对象
alex = Login_in(username,password)

alex_read = alex.read()
print(alex_read)


