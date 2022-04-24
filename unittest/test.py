import unittest
from selenium import webdriver
from time import sleep


class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")
        # self.driver.implicitly_wait(10)

    def testBaidu(self):
        '''百度搜索CSDN'''
        driver = self.driver
        driver.find_element_by_css_selector("#kw").clear()
        driver.find_element_by_css_selector("#kw").send_keys("csdn")
        driver.find_element_by_css_selector("#su").click()
        sleep(5)
        title=driver.title
        self.assertEqual(title,"csdn_百度搜索")
        sleep(5)
        driver.find_element_by_partial_link_text("CSDN").click()
        sleep(5)

    def tearDown(self):
        self.driver.quit()
