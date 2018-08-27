#!/usr/bin/python
# -*- coding: utf-8 -*-
#定期查看系统平均值
#yousong.xiang QQ:250919938 2018.8.20
#v1.0.1
#1.修改固定时间内发送邮件
#2.修改发送cpu值最高的时间
#3.修复cpu负载
#定义存放cpu负载的值
import time,commands,socket,smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header


dc = {}

now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
f1 = open('/proc/loadavg','r')
allavg = f1.readline()
load_1 = allavg.split()[0]
print load_1,now_time
dc[load_1] = now_time
f1.close()

print dc


#各个子系统
def xc_logs():
    a = os.popen('find /data/www/*/storage/logs -type d')
    line = a.readlines()
    for i in line:
        /data/script/logs_check.py i.replace('\n','')