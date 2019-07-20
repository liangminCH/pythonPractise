from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

#Open the url
driver.get("http://www.baidu.com")

# max in windows operator
driver.maximize_window()

#Get Title
baiduTitle = driver.title
print(baiduTitle)

# Get Current URL
currentUrl = driver.current_url
print(currentUrl)

# Browser Refresh
driver.refresh()
sleep(2)

#Open another URL
driver.get("http://www.google.com")
sleep(2)

#Browser back
driver.back()
sleep(2)

#Browser Forward
driver.forward()

#Get page Source 获取源代码
pageSource = driver.page_source
print(pageSource)

driver.close()#关闭当前标签
# driver.quit()#关闭整个浏览器