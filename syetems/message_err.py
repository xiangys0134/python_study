#!/usr/bin/python
# -*- coding: utf-8 -*-

import re,os

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header

##邮件发送
##user,pwd,to,header_txt,content_txt
def msg_send(user,pwd,to,header_txt,content_txt,fulltxt):
    msg = MIMEMultipart()
    msg['Subject'] = Header(header_txt,'utf-8')
    msg['From'] = Header(user)

    content1 = MIMEText(content_txt,'plain', 'utf-8')
    msg.attach(content1)

    att = MIMEText(open(fulltxt, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=fulltxt)
    msg.attach(att)

    s = smtplib.SMTP('smtp.sina.com')
    s.set_debuglevel(1)
    s.starttls()
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()



file1 = "D:\messages"
file2 = "D:\messages_new"
##打开源文件及目标文件
if os.path.exists(file1):
    f1 = open(file1, "r")
else:
    print "查询文件异常"
    exit(4)
if os.path.exists(file2):
    os.remove(file2)
    f2 = open(file2, "a+")
else:
    f2 = open(file2, "a+")

count = 0
for line in f1:
    if "centos1" in line or "DHCPREQUEST" in line:
        f2.write(line)
        count += 1

f1.close()
f2.close()
print count
if count > 0:
    print "存在报错日志...."
    count = str(count)
    msg_send('xiangys_0134@sina.com', 'meiyoumima~!@0', ['250919938@qq.com'], "存在日志错误", count,file2)




