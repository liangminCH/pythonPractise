from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.douban.com")
driver.find_element_by_class_name('lnk-movie').click()
# #这边class name正好只有一个，所以可以使用，但是一般class name都有重复的，不能唯一确定



















