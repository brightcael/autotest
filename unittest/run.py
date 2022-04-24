import unittest
from HTMLTestRunnerCN import HTMLTestReportCN
import time
from test import *

test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='daily_test.py')

if __name__ == '__main__':
    report_dir = '..'
    now = time.strftime("%Y%m%d%H%M%S")
    report_name = report_dir + "/" + now + "测试报告.html"
    with open(report_name, "wb") as f:
        runer = HTMLTestReportCN.HTMLTestRunner(stream=f,
                                                  title="自动化测试报告",
                                                  description="详细测试用例结果",
                                                  tester="锄禾")
        runer.run(discover)
    f.close()

