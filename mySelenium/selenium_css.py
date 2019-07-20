from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_css_selector('#kw').send_keys('helloworld\n') # 加一个回车键
driver.close()#关闭当前标签





