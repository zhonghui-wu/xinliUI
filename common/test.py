# from selenium import webdriver
#
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(5)
# driver.maximize_window()
# driver.get("https://admin.xinli.callwine.net/#/login")
# driver.find_element_by_css_selector(" div.tab-item.phone-way").click()
# driver.find_elements_by_css_selector(' div > input')[0].send_keys("13763910426")
# driver.find_elements_by_css_selector(' div > input')[1].send_keys("000000")
# driver.find_element_by_css_selector(" div.loginBtn.xl-button--primary").click()


def a(*args):
    b = 1
    c = args
    print(type(c))
    print(f"这是第{b}个{c[0]}")

a(12)