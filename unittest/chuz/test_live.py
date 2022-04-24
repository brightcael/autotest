import logging
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import sys
sys.path.append("..")
from parameters import login_information,chuz_exp
from utils import login,function

logging.basicConfig(
    level=logging.INFO,  # 控制台打印的日志级别
    filename='live_test.log',
    filemode='a',
    format=
        '%(asctime)s    %(message)s'
    # 日志格式
)

class Testlive(unittest.TestCase):
    def setUp(self):
        self.browser = function.browser.launch(login_information.url_info.live_website_url)
        print(type(self.browser))
    def testlive(self):
        sleep(10)
        browser = self.browser
        title = browser.title
        self.assertEqual(title, "LinkLab实验直播平台")
        logging.info('live test' + ' succsess')
    def tearDown(self):
        self.browser.quit()
