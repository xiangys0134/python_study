#!/usr/bin/python
# -*- coding: utf-8 -*-
# 邮件发送脚本
# Author Yusin
# Date 2021.3.24
# v1.0.1
# 使用方式：
# python /data/scripts/send_msg.py ['250919938@qq.com'] "** $NOTIFICATIONTYPE$ Host Alert: $HOSTNAME$ is $HOSTSTATE$ **" "$NOTIFICATIONTYPE$ $HOSTNAME$ $HOSTSTATE$ $HOSTADDRESS$ $HOSTOUTPUT$ $LONGDATETIME$"

import smtplib,sys,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

ARG1= sys.argv[1]
ARG2= sys.argv[2]
ARG3= sys.argv[3]
ARG4= sys.argv[4]
ARG5= sys.argv[5]
ARG6= sys.argv[6]
ARG7= sys.argv[7]
ARG8= sys.argv[8]

l1 = []
for arg in ARG3.split(' '):
    print(arg)
    l1.append(arg)
# ARG.pop(0)
str_email = ARG1.strip('[]')
# print(str_email)
email_user = []
for user in str_email.split(','):
    email_user.append(user)

# def execcmd(msg_str):
#     msg = os.popen('printf {}'.format(msg_str))
#     return msg.read()

def msg_send(to,header_txt,content_txt):
    # user = 'xiangys_0134@sina.com'
    user = 'xiangys0134@sina.com'
    # pwd = 'meiyoumima~!@0'
    pwd = 'XIANGys*834752'
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
    msg = '''
***** Nagios *****

{}
{}
{}
{}
{}

{}

    '''.format(ARG3,ARG4,ARG5,ARG6,ARG7,ARG8)
    content_txt = msg
    header_txt = ARG2
    # print('content_txt:',content_txt)
    # print('header_txt:',header_txt)
    msg_send(email_user, header_txt, content_txt)