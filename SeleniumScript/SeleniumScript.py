from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\Ashu\\Documents\\selenium_driver\\chromedriver.exe")
driver.set_page_load_timeout(30)
driver.get("http://wwww.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.get_screenshot_as_file("Facebook.png")
driver.quit()

