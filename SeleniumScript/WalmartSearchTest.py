
"""
The code takes the site http://www.walmart.com on chrome browser, clicks on
search bar, type "laptop", clicks on search button and clicks on sort drop down menu.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time


class WalmartSearchTest:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-error')
        options.add_argument("--ignore-ssl-errors")
        options.add_argument(os.path.realpath(__file__))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedrive = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedrive
        self.driver = webdriver.Chrome(chrome_options=options,
                                       executable_path="c:\\users\\ashu\\documents\\selenium_driver\\chromedriver.exe")

    def timepractice(self):
        time.sleep(10)

    def gotowalmart(self):
        self.driver.get("http://www.walmart.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)

        self.driver.find_element_by_id("global-search-input").send_keys("laptop")
        # self.driver.switch_to.frame(self.driver.find_element_by_class_name("header-search-button"))
        self.driver.find_element_by_css_selector(".elc-icon.elc-icon-search").click()  # use css selector if you get
        # Message: invalid selector: Compound class names not permitted
        self.driver.find_element_by_css_selector(".chooser-option-current").click()

        # self.driver.back()
        # self.driver.forward()
        # time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    obj = WalmartSearchTest()
    obj.gotowalmart()
