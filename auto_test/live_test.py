import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
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

def live_test():
    try:
        browser = function.browser.launch(login_information.url_info.live_website_url)
        sleep(20)
        logging.info('live test' + ' succsess')
    except Exception as e:
        logging.info('live test' + ' failed\n'+str(e))
if __name__ == "__main__":
    logging.info("----------------test start------------------")
    live_test()
    logging.info("----------------test end------------------")