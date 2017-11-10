#!/usr/bin/env python
# coding:utf-8
import unittest
import time
import requests

class MyTest(unittest.TestCase):
    def setUp(self):
        print u'查询快递开始'
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        danhao = '1202247993797'
        kd = u'yunda'
        self.url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-%s-%s.html' % (danhao, kd)
    def tearDown(self):
        time.sleep(1)
        print u'查询快递结束'

class IntegerArithmeticTestCase(MyTest):
    u'''快递接口查询'''
    def test_yunda(self): ## test method names begin 'test*'
        u'''韵达快递情况'''
        r = requests.get(self.url,headers=self.headers,verify=False)
        result = r.json()
        print result['company']
        data = result['data']
        get_result = data[0]['context']
        print get_result
        self.assertEqual(u"韵达快递",result['company'])
        self.assertIn(u"已签收",get_result)

if __name__ == '__main__':
    unittest.main()