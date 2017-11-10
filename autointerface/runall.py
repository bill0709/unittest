#!/usr/bin/env python
# #coding:utf-8
import unittest
import time
test_dir ='./'

discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    time.sleep(1)
    runner.run(discover)

