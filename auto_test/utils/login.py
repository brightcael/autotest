from time import ctime, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
def login(username,password,browser):
    button = browser.find_element_by_xpath('//*[@id="components-layout-demo-top"]/header/div/ul/li[2]')
    button.click()

    ###输入用户名
    ident = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[1]/div/div/span/span/input')
    ident.send_keys(username)

    ###输入密码
    pwd = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[2]/div/div/span/span/input')
    pwd.send_keys(password)

    # pulldown=browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div/input')
    # pulldown.click()
    sleep(2)
    ###站点选择
    # =browser.find_element_by_xpath(site['linklab'])
    # site_choose.click()
    ###

    login = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[4]/div/div/span/button')
    login.click()
    sleep(2)

def login_cz_branch(username,password,browser):
    button = browser.find_element_by_xpath('/html/body/div/div/section/header/div/ul/li[4]')
    button.click()

    ###输入用户名
    ident = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[1]/div/div/span/span/input')
    ident.send_keys(username)

    ###输入密码
    pwd = browser.find_element_by_xpath('/html/body/div[1]/div/div/div/div/form/div[2]/div/div/span/span/input')
    pwd.send_keys(password)
    # pulldown=browser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div[2]/div/div/div[3]/div[1]/div[2]/div[1]/div/div/input')
    # pulldown.click()
    sleep(2)
    ###站点选择
    # =browser.find_element_by_xpath(site['linklab'])
    # site_choose.click()
    ###

    login = browser.find_element_by_xpath('//*[@id="app"]/div/div/div/div/form/div[4]/div/div/span/button')
    login.click()
    sleep(2)

def enter_course(browser,c_path):
    course_button = browser.find_element_by_xpath(c_path)
    course_button.click()
    sleep(2)