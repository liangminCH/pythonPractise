from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.google.com")
# driver.find_element_by_xpath("//a[@class='gb_z gb_pc']").click()
driver.find_element_by_xpath("//a[contains(text(),'Gmail')]").click()




























