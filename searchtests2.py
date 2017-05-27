#!/user/bin/env python
#encoding: utf-8

import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 基于类的setUp()和tearDown()方法
        # 这里的‘@classmethod’支持在一个类中只进行一次初始化和清理
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get("http://www.jd.com/")

    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("key")
        self.search_field.clear()
        self.search_field.send_keys("phones")

        #submit
        self.search_btn = self.driver.find_element_by_xpath("//button[@clstag='h|keycount|2015|03c']")
        self.search_btn.click()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 3, "more than 3~~")

    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id("key")
        self.search_field.clear()
        self.search_field.send_keys("android")

        #submit
        self.search_btn = self.driver.find_element_by_xpath("//button[@clstag='shangpin|keycount|toplist1|b03']")
        self.search_btn.click()


        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 4, "more than 4~~")

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)