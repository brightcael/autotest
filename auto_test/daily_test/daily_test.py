import logging
import unittest
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
####本地文件
import config
import sys
sys.path.append("..")
from parameters import login_information
from utils import login,function
####日志格式定义
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename='daily_test.log',
                            filemode='a',
                            format=
                            '%(asctime)s    %(message)s'
                            # 日志格式
                            )
######导入参数
list = config.exp.exp_info
class chuz_test(unittest.TestCase):
    def setUp(self):
        try:
            self.browser = function.browser.launch(login_information.url_info.formal_website_url)

            login.login(login_information.account_info.newtest['username'],
                                  login_information.account_info.newtest['pwd'],self.browser)
            login.enter_course(self.browser, config.exp.course_path)
        except Exception as e:
            logging.info("login failed!\nraw error:"+str(e))

    def testCourse1(self,exp=list[0]):
        sleep(1)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(1)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(3)
        start_exp = self.browser.find_element_by_xpath('/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning',result1)
        print(result1)
        self.browser.quit()

    def testCourse2(self, exp=list[1]):
        sleep(2)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = self.browser.find_element_by_xpath(
            '/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning', result1)
        print(result1)
        self.browser.quit()

    def testCourse3(self,exp=list[2]):
        sleep(2)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = self.browser.find_element_by_xpath('/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning',result1)
        print(result1)
        self.browser.quit()

    def testCourse4(self,exp=list[3]):
        sleep(2)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = self.browser.find_element_by_xpath('/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning',result1)
        print(result1)
        self.browser.quit()

    def testCourse5(self,exp=list[4]):
        sleep(2)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = self.browser.find_element_by_xpath('/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning',result1)
        print(result1)
        self.browser.quit()

    def testCourse6(self,exp=list[5]):
        sleep(2)
        chapter_but = self.browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = self.browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = self.browser.find_element_by_xpath('/html/body/div/section/main/div/div/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = self.browser.current_window_handle
        print(2)
        self.browser.switch_to.window(self.browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = self.browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = self.browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(30)

        ##读取结果并返回
        udcshell = self.browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        self.assertIn('burning',result1)
        print(result1)
        self.browser.quit()

    def tearDown(self):
        self.browser.quit()
