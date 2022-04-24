import unittest
import time
import daily_test
import sys
sys.path.append("..")
from parameters import login_information,chuz_exp
from utils import login,function
from HTMLTestRunnerCN import HTMLTestReportCN

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='daily_test.py')
exp=[]
if __name__ == "__main__":
    exp = list
    print(exp)
    report_dir = './reports'
    now = time.strftime("%Y%m%d%H%M%S")
    report_name = report_dir + "/" + now + "测试报告.html"
    with open(report_name, "wb") as f:
        runer = HTMLTestReportCN.HTMLTestRunner(stream=f,
                                                title="自动化测试报告",
                                                description="详细测试用例结果",
                                                tester="李皓宇")
        runer.run(discover)
    f.close()

    # report_dir = '../chuz'
    # now = time.strftime("%Y%m%d%H%M%S")
    # report_name = report_dir + "/" + now + "测试报告.html"
    # with open(report_name, "wb") as f:
    #     runer = HTMLTestReportCN.HTMLTestRunner(stream=f,
    #                                             title="自动化测试报告",
    #                                             description="详细测试用例结果",
    #                                             tester="锄禾")
    #     runer.run(discover)
    # f.close()