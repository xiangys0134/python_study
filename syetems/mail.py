#!/usr/bin/python
# -*- coding: utf-8 -*-


#定期查看系统平均值
#yousong.xiang QQ:250919938 2018.8.16
#v1.0.1
#定义存放cpu负载的值
import time,commands,socket,smtplib
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header

cpu_load = []

##邮件发送
##user,pwd,to,header_txt,content_txt
#def msg_send(user,pwd,to,header_txt,content_txt,fulltxt):
def msg_send(user,pwd,to,header_txt,content_txt):
    msg = MIMEMultipart()
    msg['Subject'] = Header(header_txt,'utf-8')
    msg['From'] = Header(user)

    content1 = MIMEText(content_txt,'plain', 'utf-8')
    msg.attach(content1)

    #att = MIMEText(open(fulltxt, 'rb').read())
    #att.add_header('Content-Disposition', 'attachment', filename=fulltxt)
    #msg.attach(att)

    #s = smtplib.SMTP('smtp.sina.com')
    s = smtplib.SMTP_SSL('smtp.163.com',465)
    s.set_debuglevel(1)
    s.starttls()
    s.login(user, pwd)
    s.sendmail(user, to, msg.as_string())
    s.close()


#获取本地主机名、IP地址
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

#获取本机计算机名
myname = commands.getstatusoutput('hostname')[1]
#获取本机IP地址
myaddr = get_host_ip()


#获取cpu负载信息
def load_avg():
    f1 = open('/proc/loadavg','r')
    allavg = f1.readline()
    load_1 = allavg.split()[0]
    return load_1


# flag = 1
# while True:
#     cpu_load.append(load_avg())
#     if flag == 60:
#         cpuload_max = max(cpu_load)
#         flag=0
#         #print cpuload_max,cpu_load
#         msg_send('xiangys_0134@sina.com', 'meiyoumima~!@0', ['xiangys0134@sina.com','250919938@qq.com'],myaddr + myname + '当前1小时内最高负载','CPU负载：' + cpuload_max)
#         cpu_load = []
#     time.sleep(60)
#     flag += 1

#msg_send('xiangys_0134@sina.com', 'meiyoumima~!@0', ['xiangys0134@sina.com', '250919938@qq.com'],'当前1小时内最高负载', 'CPU负载：')
msg_send('xiangys0134@163.com', 'XIANGys*44767870', ['xiangys0134@sina.com', '250919938@qq.com'],'当前1小时内最高负载', 'CPU负载：')