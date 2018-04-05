from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Users\\Ashu\\Documents\\selenium_driver\\geckodriver.exe")

driver.set_page_load_timeout(40)
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file(".\\ScreenShots\\Facebook.png")
print(driver.title)
assert "Facebook" in driver.title
driver.find_element_by_id("email").send_keys("FacebookLogin")
driver.find_element_by_id("pass").send_keys("Facebook")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file(".\\ScreenShots\\Facebook1.png")
driver.quit()

