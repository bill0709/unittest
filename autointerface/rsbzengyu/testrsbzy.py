#!/usr/bin/env python
# #coding:utf-8
import json,requests
import unittest


class MyTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://123.57.225.54:8018/giftRSB'
        self.lx  = {'content-type': 'application/json'}
        self.data = json.dumps({'userId': '17592', 'isId': 'Z1000592150', 'channelId': '1001', 'toUserId': '10285', 'amount': "100",
                "password": "666666", "phone": "17310024144"})
        print u'赠与开始'
    def tearDown(self):
        print u'赠与结束'
class TestAdd(MyTest):
    u'''荣盛币赠与接口'''
    def testZengyu(self):
        u'''赠与荣盛币测试'''
        r = requests.post(self.url, self.data, headers=self.lx)
        self.assertIn(r.json()['message'], u'成功')
        print u'断言通过'

if __name__ == '__main__':
    unittest.main()