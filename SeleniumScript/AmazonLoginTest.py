
"""
The below code takes you to the site http://www.amazon.com on chrome browser, click on
Account> Sign In> fills in Email Address box as "yourcorrectemailaddress@gmail.com",
Password box as "YourCorrectPassword" and click on Sign In button.
Make sure you have enter correct username and password.
"""


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time


class AmazonLoginTest:

    def __init__(self):

        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-error')
        options.add_argument("--ignore-ssl-errors")
        options.add_argument(os.path.realpath(__file__))
        dir_path = os.path.dirname(os.path.realpath(__file__))
        chromedrive = dir_path + "/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedrive
        self.driver = webdriver.Chrome(chrome_options=options,
                                       executable_path="C:\\Users\\Ashu\\Documents\\selenium_driver\\chromedriver.exe")

    def timePractice(self):
        time.sleep(10)

    def gotoamazon(self):
        self.driver.get("http://www.amazon.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        ui.WebDriverWait(self.driver, 35).until(EC.visibility_of_element_located((By.ID, "nav-link-accountList")))
        self.driver.find_element_by_id("nav-link-accountList").click()
        # ui.WebDriverWait(self.driver, 35).until(EC.visibility_of_element_located((By.ID, "account-signin")))
        # self.driver.find_element_by_id("account-signin").click()
        self.driver.find_element_by_id("ap_email").send_keys("george_costanza@yahoo.com") # Make sure the email is
        # valid or else it won't got to the password page.
        self.driver.find_element_by_id("continue").click()
        self.driver.find_element_by_id("ap_password").send_keys("ItsNotYouItsMe#")
        self.driver.find_element_by_id("signInSubmit").click()
        self.driver.quit()

        # ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "tab-flight-tab-hp")))
        # self.driver.find_element_by_id("tab-flight-tab-hp").click()  # clicks on the flights button.
        # time.sleep(10)

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    obj = AmazonLoginTest()
    obj.gotoamazon()





