import logging
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
# import sys
# sys.path.append("..")
from parameters import login_information,chuz_exp
from utils import login,function

####日志格式定义
logging.basicConfig(level=logging.INFO,  # 控制台打印的日志级别
                            filename='chuz_test.log',
                            filemode='a',
                            format=
                            '%(asctime)s    %(message)s'
                            # 日志格式
                            )

def chuz_test(exp):
    print(exp["name"]+"start")
    try:
        browser = function.browser.launch(login_information.url_info.chuzhou_website_url)
        login.login_cz_branch(login_information.account_info.teacherAC['username'],login_information.account_info.teacherAC['pwd'], browser)
        login.enter_course(browser,chuz_exp.exp.course_path)

        sleep(2)
        chapter_but = browser.find_element_by_xpath(exp['chapter'])
        chapter_but.click()

        sleep(2)
        exp_but = browser.find_element_by_xpath(exp['exp'])
        exp_but.click()

        sleep(2)
        start_exp = browser.find_element_by_xpath('/html/body/div/section/main[2]/div/div[1]/div[2]/form/div[5]/div/button')
        start_exp.click()

        sleep(15)
        print(3)
        homepage = browser.current_window_handle
        print(2)
        browser.switch_to.window(browser.window_handles[-1])
        print(1)

        ###webide

        title = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="device-view"]/div[1]/div/div[1]/div/div/div[1]/h4'))
        )
        btnsubmit = browser.find_element_by_xpath('//*[@id="submitSrcButtonexperiment"]')
        js4 = "arguments[0].scrollIntoView();"
        browser.execute_script(js4, btnsubmit)
        btnsubmit.click()
        sleep(3)

        ###编译烧写
        alertObject = browser.switch_to.alert
        print(alertObject.text)
        alertObject.accept()
        sleep(40)

        ##读取结果并返回
        udcshell = browser.find_element_by_xpath('//*[@id="udc-shell"]')
        result1 = udcshell.text
        print(result1)
        logging.info(str(exp['name']) + '  success\n')
        browser.quit()

    except Exception as e:
        print(1)
        logging.info(str(exp['name'])+'   failed\n'+str(e))
if __name__ == "__main__":
    logging.info("----------------test start------------------")
    for list in chuz_exp.exp.exp_info:
        chuz_test(list)
    logging.info("----------------test end------------------")