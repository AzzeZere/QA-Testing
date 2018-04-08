
"""
The code below will take to the site http://www.expedia.com on chrome browser, fills in the Origin, Destination,
Departing, Returning, Traveler information and click on Search button.
"""



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
import os
import time


class expediaUnitTest():

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

    def gotoexpedia(self):
        self.driver.get("http://www.expedia.com/")
        # self.driver.maximize_window()
        # self.driver.implicitly_wait(20)
        ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "tab-flight-tab-hp")))
        self.driver.find_element_by_id("tab-flight-tab-hp").click()
        # ui.WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.ID, "package-origin-hp-package")))
        # self.driver.find_element_by_id("package-origin-hp-package").send_keys('Seattle, Washington')
        # self.driver.find_element_by_id("package-destination-hp-package").send_keys('Dallas, Texas')
        # self.driver.find_element_by_id("package-departing-hp-package").send_keys('4/18/2018')
        # self.driver.find_element_by_id("package-returning-hp-package").send_keys('5/12/2018')
        # self.driver.find_element_by_id('search-button-hp-package').click()
        # time.sleep(20)

        parentTab = self.driver.find_element_by_id('flightModuleList')
        for selectAll in parentTab.find_element_by_xpath("//*"):
            if selectAll.get_attribute("class") == 'dollars price-emphasis':
                print(selectAll.get.attribute("class"))

    def teardown(self):
        self.driver.close()


if __name__ == "__main__":
    obj = expediaUnitTest()
    obj.gotoexpedia()




