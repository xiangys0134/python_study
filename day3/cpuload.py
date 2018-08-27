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

cpu_load = []


##邮件发送
def msg_send(user,password,receivers,title,content):
    # 第三方 SMTP 服务
    mail_host = "smtp.qiye.163.com" # SMTP服务器
    #mail_user = "ops@xuncetech.com" # 用户名
    #mail_pass = ".FgX~/D?Lrhvun;" # 密码

    #sender = 'ops@xuncetech.com' # 发件人邮箱(最好写全, 不然会失败)
    sender = user # 发件人邮箱(最好写全, 不然会失败)
    #receivers = ['250919938@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #content = '过期教程害死人!'
    #title = 'Python SMTP Mail Test' # 邮件主题
    message = MIMEText(content, 'plain', 'utf-8') # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465) # 启用SSL发信, 端口一般是465
        smtpObj.login(user, password) # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string()) # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


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

dc = {}
#获取cpu负载信息
def load_avg():
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    f1 = open('/proc/loadavg','r')
    allavg = f1.readline()
    load_1 = allavg.split()[0]
    dc[load_1] = now_time
    f1.close()
    #return load_1


flag = 1
while True:
    load_avg
    #cpu_load.append(load_avg())
    if flag == 60:
        cpuload_max = max(dc)
        flag=0
        print cpuload_max,dc[cpuload_max]
        msg_send('ops@xuncetech.com', '.FgX~/D?Lrhvun;', ['xiao.li@xuncetech.com','yousong.xiang@xuncetech.com','shaobo.zheng@xuncetech.com','song.wu@xuncetech.com'],myaddr + myname + '当前12小时内最高负载','CPU负载：' + cpuload_max + '时间：' + dc[cpuload_max])
        cpu_load = []
    time.sleep(60)
    flag += 1