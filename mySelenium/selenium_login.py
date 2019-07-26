from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get('https://etax.anhui.chinatax.gov.cn/')
driver.maximize_window()
driver.find_element_by_id("login").click()
WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('loginSrc'))
driver.switch_to.frame('loginSrc')
driver.find_element_by_xpath("//dd[@class='util_tab_head_list login_active']").click()

driver.find_element_by_id('username').send_keys('913401000723758800')
driver.find_element_by_id('password').send_keys('a1234567')
driver.execute_script('$("#vc1").data("sliderVc").setSession();') #滑动滑块
driver.find_element_by_xpath("//form[@id='fm2']//a[@class='login_btn sub_btn fr w95']").click()


uri = "/sb/wssb/statistic/ysbxxNsr"
driver.execute_script('''location.href="{url}";'''.format(url=uri))
WebDriverWait(driver, 20).until(
   lambda driver: driver.find_element_by_xpath("//form[@id='initForm']/table[2]//tr/td[3]/input[@value='汇总统计/打印']"))

#driver.execute_script('$(".hasDatepicker:eq(0)").val("2018-01-01");')
#driver.execute_script('$(".hasDatepicker:eq(1)").val("2018-12-31");')

#driver.execute_script("$(\"[name = 'zsxmDm']\").val('10101')")
#Select(driver.find_element_by_id("zsxmDm")).select_by_visible_text("增值税")
#driver.execute_script('$(".validatebox-text:eq(0)").val("增值税")')
# driver.find_element_by_xpath("//form[@id='initForm']/table[2]//tr/td[1]/input[@value='查询']").click()

# WebDriverWait(driver, 20).until(
#    lambda driver: driver.find_element_by_link_text("我要查询"))
# driver.execute_script('''jQuery("a[title='我要查询']").trigger("blur").trigger("click")''')
# driver.execute_script('''jQuery("a[title='申报信息查询']").trigger("blur").trigger("click")''')
# driver.execute_script('''jQuery("a[title='已申报信息查询（税收）']").trigger("blur").trigger("click")''')
#
# # WebDriverWait(driver, 20).until(
#    lambda driver: driver.find_element_by_xpath("//body/table[@class='table_all_border']//td[@class='td_table_top']"))

# driver.switch_to.frame('layui-layer22')

name='增值税'
sbqs='2018-01-01'
sbqz='2018-12-31'
driver.execute_script('''$(".hasDatepicker:eq(0)").val("{sbqs_date}");'''.format(sbqs_date=sbqs))
driver.execute_script('''$(".hasDatepicker:eq(1)").val("{sbqz_date}");'''.format(sbqz_date=sbqz))
if name == "增值税":
    driver.execute_script("$(\"[name = 'zsxmDm']\").val('10101')")
driver.find_element_by_xpath("//form[@id='initForm']/table[2]//tr/td[1]/input[@value='查询']").click()
WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_link_text('查看'))

# 获取当前窗口句柄（窗口A）
handle = driver.current_window_handle

#更改打开窗口
# driver.execute_script("parent.openWindow2 = window.open;")
# dfg= 1
# driver.execute_script('''openCell('/sb','{dd}');'''.format(dd=dfg))

for tr in driver.find_elements_by_tag_name("tr"):
    td_list = tr.find_elements_by_tag_name("td")
    try:
        if sbqs <= td_list[4].text.strip() <= sbqz and td_list[1].text.strip()=="增值税纳税申报表（一般纳税人适用）":
            click_in = td_list[7].find_element_by_tag_name("a").get_attribute("onclick")
            driver.execute_script("parent.openWindow2 = window.open;")
            driver.execute_script(click_in)
            break
    except:
        pass

# sleep(3)
# lcl = driver.execute_script("return document.location.href")
# print(lcl)


# 获取当前所有窗口句柄（窗口A、B）
handles = driver.window_handles

# 对窗口进行遍历
for newhandle in handles:
    if newhandle!=handle:
        # 切换到新打开的窗口B
        driver.switch_to.window(newhandle)

WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('button.printBtn'))
#driver.find_element_by_xpath("//button[@class='printBtn']").click()
driver.switch_to.window(handle)
driver.switch_to.window(newhandle)

