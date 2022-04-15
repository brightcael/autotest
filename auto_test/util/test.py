from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import json
import time
import hmac
import hashlib
import base64
import urllib.parse
import logging
###本地文件

import login
import function
import sys
sys.path.append("..")
from parameters import login_information




###参数
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename='chuz_exp.log',
                            filemode='a',
                            format=
                            '%(asctime)s    %(message)s'
                            # 日志格式
                            )
def test():

    browser = function.browser.launch(login_information.url_info.chuzhou_website_url)
    login.login_cz_branch(login_information.account_info.teacherAC['username'],login_information.account_info.teacherAC['pwd'], browser)

if __name__ == "__main__":
    test()

