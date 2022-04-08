from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from xinliUI.utils.get_yaml import get_yaml_data


driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.set_window_size(1920,1080)
driver.get("https://admin.xinli.callwine.net/#/login")
driver.find_element_by_css_selector(" div.tab-item.phone-way").click()
driver.find_elements_by_css_selector(' div > input')[0].send_keys("13763910426")
driver.find_elements_by_css_selector(' div > input')[1].send_keys("000000")
driver.find_element_by_css_selector(" div.loginBtn.xl-button--primary").click()
# sleep(1)
ele = driver.find_element_by_css_selector('ul:nth-child(2) > li > div > span')
ActionChains(driver).move_to_element(ele).perform()
driver.find_element_by_xpath('//li[text()="退出"]').click()

# driver.find_element_by_xpath('//li[3]/div').click()
# driver.find_element_by_css_selector('li.el-submenu.is-opened > ul > li:nth-child(1)').click()

# driver.find_element_by_css_selector('form > div:nth-child(2) > div > div > input').send_keys(111)
# driver.find_element_by_css_selector('form > div:nth-child(4) > div > div').click()
# name = driver.find_element_by_xpath('//div[3]/div[1]/div[1]/ul/li[1]').text
# driver.find_element_by_xpath('//div[3]/div[1]/div[1]/ul/li[1]').click()
# print(name)
# print(driver.find_element_by_xpath('//div[3]/table/tbody/tr[1]/td[1]/div').text)
# driver.find_element_by_css_selector('li.el-submenu.is-opened > ul > li:nth-child(2)').click()


