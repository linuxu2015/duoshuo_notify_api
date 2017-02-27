#!/usr/bin/env python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def email(message):
    #构造MIMEText对象,第一个参数就是邮件正文,第二个参数是MIME的subtype
    # 传入'plain'，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性。
    msg = MIMEText(message, 'plain', 'utf-8')   #message为传入的参数,为发送的消息.
    """msg = MIMEText('<html><body><h1>Hello</h1>' +
    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
    '</body></html>%s' %message, 'html', 'utf-8')"""
    #标准邮件需要三个头部信息： From, To, 和 Subject。
    msg['From'] = formataddr(["多说评论通知",'xulibao@everyoo.com'])     #显示发件人信息
    msg['To'] = formataddr(["QQ",'371044414@qq.com'])          #显示收件人信息
    msg['Subject'] = "多说评论通知"      #定义邮件主题
    try:
        #创建SMTP对象
        server = smtplib.SMTP("smtp.aioute.com", 25)
        #set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
        #server.set_debuglevel(1)
        #login()方法用来登录SMTP服务器
        server.login("xulibao@everyoo.com","123456")
        #sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
        server.sendmail('xulibao@everyoo.com', ['371044414@qq.com',], msg.as_string())
        print u"邮件发送成功!"
        server.quit()
    except smtplib.SMTPException:
        print u"Error: 无法发送邮件"
if __name__ == '__main__':
    cpu = 100
    disk = 50
    mem = 50
    for i in range(1):
        if cpu > 90:
            alert = u"CPU出问题！"
            email(alert)
        if disk > 90:
            alert = u"硬盘出问题！"
            email(alert)
        if mem > 80:
            alert = u"内存出问题！"
            email(alert)
