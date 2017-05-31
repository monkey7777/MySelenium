#!/user/bin/env python
#encoding: utf-8

import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        #create a new Firefox session
        #firefox_driver_path = r"C:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # chrome_driver_path = r"C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        # options = webdriver.ChromeOptions()
        # options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        # self.driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
        # self.driver.get("https://www.baidu.com")

        # navigate to the application home Page
        self.driver.get("http://www.jd.com/")

    def test_search_by_category(self):
        #keywords
        self.search_field = self.driver.find_element_by_id("key")
        self.search_field.clear()
        self.search_field.send_keys("phones")

        #go search
        self.search_btn = self.driver.find_element_by_xpath("//button[@clstag='h|keycount|2016|03c']")
        self.search_btn.click()

        #获取页面所有商品的 <a>标签ַ
        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 3, "more than 3~~")


    def test_search_by_name(self):
        #输入搜索关键字
        self.search_field = self.driver.find_element_by_id("key")
        self.search_field.clear()
        self.search_field.send_keys("phones")

        #go search
        self.search_btn = self.driver.find_element_by_xpath("//button[@clstag='h|keycount|2016|03c']")
        self.search_btn.click()

        products = self.driver.find_elements_by_xpath("//div[@class='p-img']/a")
        self.assertGreater(len(products), 4, "more than 4~~")

    def tearDown(self):
        # close
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)