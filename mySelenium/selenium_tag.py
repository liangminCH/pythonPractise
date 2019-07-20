from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.baidu.com")
elements = driver.find_elements_by_tag_name('a')

for element in elements:
    # if '新闻' in element.text:
    #     element.click()
    print(element)
    print(element.text)

driver.quit()



