# 用ID定位
# 类似 document.getElementById("username")
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
driver  = webdriver.Chrome()
driver.get("https://etax.anhui.chinatax.gov.cn/")
driver.maximize_window()
#driver.fullscreen_window()
driver.find_element_by_id('login').click()
print("login success")
WebDriverWait(driver,20).until(lambda driver:driver.find_element_by_id('loginFrame'))
print("1")
driver.execute_script('$("dd[title=\'普通用户\']").click();')
print('2')
#driver.find_element_by_id('username').send_keys('91340600MA2RYT114E')
#driver.find_element_by_id('password').send_keys('JXT111111')
driver.execute_script('$("#username").val("91340600MA2RYT114E");$("#password").val("JXT111111");')
print('3')
driver.execute_script('$("#vc1").data("sliderVc").setSession();')
driver.execute_script("login('fm2');")















