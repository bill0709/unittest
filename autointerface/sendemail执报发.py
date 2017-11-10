#!/usr/bin/env python
#coding:utf-8

from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib,unittest,time,os

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    f.close()
    #发送内容
    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header(u"自动化测试报告", 'utf-8')
    #发送准备
    msg['from'] = 'weihaitao0510@163.com'
    tolist = ['411141606@qq.com','weihaitao@4zlink.com','weihaitao0510@163.com']
    msg['to'] = ','.join(tolist)
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('weihaitao0510@163.com','weihaitao91123')
    smtp.sendmail(msg['from'], tolist, msg.as_string())
    smtp.quit()
    print 'email has send out !'

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+'\\'+fn))
    file_new = os.path.join(testreport,lists[-1])
    print file_new
    return file_new

if __name__ =='__main__':
    #先执行
    test_dir = './'
    # test_dir = 'D:\\workspace\\autointerface'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%y-%m-%d %H_%M_%S')
    fp = open('./report1/' + now + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'以下用例执行情况:')
    runner.run(discover)
    fp.close()
    #再找
    # test_report = 'D:\\workspace\\autointerface\\report1'
    test_report = './report1'
    html = new_report(test_report)
    send_mail(html)

