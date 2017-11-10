#!/usr/bin/env python
# #coding:utf-8
import unittest
import time
from HTMLTestRunner import HTMLTestRunner

test_dir ='./'
# test_dir = 'D:\\workspace\\autointerface'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    now = time.strftime('%y-%m-%d %H_%M_%S')
    fp = open('./report1/' + now + 'result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'自动化接口测试报告', description=u'以下用例执行情况:')
    runner.run(discover)
    fp.close()
    print '********'
    print 'kkkkkk'
