#!/usr/bin/python
# -*- coding: utf-8 -*-
# 邮件发送脚本
# Author Yusin
# Date 2021.3.24
# v1.0.1
# 使用方式：send_msg.py ['250919938@qq.com','xiangys0134@sina.com'] $NOTIFICATIONTYPE$ $HOSTNAME$ $HOSTSTATE$ $HOSTADDRESS$ $HOSTOUTPUT$ $LONGDATETIME$

import smtplib,sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

ARG1= sys.argv[1]
ARG2= sys.argv[2]
ARG3= sys.argv[3]


# ARG.pop(0)
str_email = ARG1.strip('[]')
# print(str_email)
email_user = []
for user in str_email.split(','):
    email_user.append(user)

class redirect:
    content = ""

    def write(self,str):
        self.content += str
    def flush(self):
        self.content = ""

def msg_send(to,header_txt,content_txt):
    user = 'xiangys_0134@sina.com'
    pwd = 'meiyoumima~!@0'
    msg = MIMEMultipart()
    msg['Subject'] = Header(header_txt,'utf-8')
    msg['From'] = Header(user)

    content1 = MIMEText(content_txt,'plain', 'utf-8')
    msg.attach(content1)

    # s = smtplib.SMTP('smtp.sina.com')
    s = smtplib.SMTP_SSL('smtp.sina.com',465)
    #s.set_debuglevel(1)              #调试使用
    #s.starttls()                    #建议使用
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()

if __name__ == '__main__':
    # header_list = ARG[0:3]
    # header_txt = '** {} Host Alert: {} is {} **'.format(*header_list)
    # content_txt = 'load gt 5'
    r = redirect()
    sys.stdout = r
    print(ARG2)
    content_txt = r.content
    content_txt = ARG2
    header_txt = ARG3
    msg_send(email_user, header_txt, content_txt)