#!/usr/bin/python
# -*- coding: utf-8 -*-
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText

fulltxt = "D:\messages_new"

mail_info = {
    "from": "xiangys_0134@sina.com",
    "to": "250919938@qq.com",
    "hostname": "smtp.sina.com",
    "username": "xiangys_0134@sina.com",
    "password": "meiyoumima~!@0",
    "mail_subject": "test",
    "mail_text": "hello, this is a test email, sended by py",
    "mail_encoding": "utf-8"
}

if __name__ == '__main__':
    # 这里使用SMTP_SSL就是默认使用465端口
    smtp = SMTP_SSL(mail_info["hostname"])
    smtp.set_debuglevel(1)

    smtp.ehlo(mail_info["hostname"])
    smtp.login(mail_info["username"], mail_info["password"])

    #msg = MIMEText(mail_info["mail_text"], "plain", mail_info["mail_encoding"])
    att = MIMEText(open(fulltxt, 'rb').read(), "plain", mail_info["mail_encoding"])
    att.add_header('Content-Disposition', 'attachment', filename=fulltxt)
    msg.attach(att)

    msg["Subject"] = Header(mail_info["mail_subject"], mail_info["mail_encoding"])
    msg["from"] = mail_info["from"]
    msg["to"] = mail_info["to"]

    smtp.sendmail(mail_info["from"], mail_info["to"], msg.as_string())

    smtp.quit()