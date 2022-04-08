from xinliUI.common.comm_driver import CommDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from xinliUI.config.config import wait_poll_frequency, wait_time
from xinliUI.utils.all_path import screenshots_path, log_save_path
from xinliUI.utils.log import log
from xinliUI.utils.get_yaml import get_yaml_data
from selenium.webdriver import ActionChains


class BasePage():
    """
    公共操作方法：
        1. 初始化得到一个浏览器
        2. 打开一个URL
        3. 获取页面上的一个元素
        4. 点击元素
        5. 在元素上输入内容
        补充:
        6. 获取元素的文本   #触发条件: 测试登录，判断登录后首页的元素文本是否是'首页'
        7. 增加一个等待元素出现后点击的方法 #触发条件点击个人中心后来不及点退出
        8. 输入了错误的用户名和密码后提示信息太快，导致无法获取到，获取元素信息也要等待
    """

    def __init__(self, yaml_path):
        """
        初始化一个浏览器,并获取elements.yaml中的定位方法和元素
        page_object的class名称要和elements.yaml的分类名称一致
        :param yaml_path: 传需要读取的elements的yaml文件
        """
        self.locators = get_yaml_data(yaml_path)[self.__class__.__name__]
        for element, locator in self.locators.items():
            setattr(self, element, locator)
        self.driver = CommDriver().get_driver()

    def open_url(self, url):
        """
        打开一个指定的url
        :param url: 指定一个url
        :return: None
        """
        self.driver.get(url)

    def get_element(self, locator):
        """
        获取一个元素
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return: 返回一个element对象
        """
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        """
        获取一个元素,返回的是一个list
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return: 返回一个element对象
        """
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """
        元素点击，支持当元素为定位到是多个的时候，也可以点击
        :param locator:  元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return:
        """
        self.get_element(locator).click()

    def input_text(self, locator, text, append=False):
        """
        输入文本
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :param text: 要输入的文本
        :param append: 是否追加输入，如果是True就追加，默认清空后再输入
        :return:
        """
        if not append:
            self.get_element(locator).clear()
            self.get_element(locator).send_keys(text)
        else:
            self.get_element(locator).send_keys(text)

    def get_element_text(self, locator):
        """
        获取一组元素的text
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return: 一组元素text的list
        """
        eles = self.get_elements(locator)
        return [ele.text for ele in eles]

    def wait_click_element(self, locator):
        """
        显示等待的点击
        :param locator:  元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return:
        """
        WebDriverWait(self.driver, timeout=wait_time, poll_frequency=wait_poll_frequency)\
            .until(EC.visibility_of_element_located(locator)).click()

    def wait_get_element_text(self, locator):
        """
        显示等待获取文本
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return: 返回文本信息
        """
        return WebDriverWait(self.driver, timeout=wait_time, poll_frequency=wait_poll_frequency) \
            .until(EC.visibility_of_element_located(locator)).text

    def isexist_element(self, locator, Action=None):
        """
        判断元素是否存在
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :param Action: 元素名称，只有会报错的时候用的上
        :return: 返回元素
        """
        try:
            element=WebDriverWait(self.driver, timeout=wait_time, poll_frequency=wait_poll_frequency) \
                .until(EC.element_to_be_clickable(locator))
            return element
        except:
            self.driver.save_screenshot(screenshots_path + f'{Action}.png')
            log(log_save_path).error(f'{Action}元素无法定位')
            return False

    def move_to_element(self, locator):
        """
        用于退出登录。移动到一个点
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return:
        """
        ele = self.get_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def get_list_elements(self, locator):
        """
        获取页面的一列内容，10个
        :param locator: 元素定位器，示例：['css selector','.el-message--error']， ['id','btnLogin']
        :return: 返回该列内容的list
        """
        ele_list = []
        for i in range(1, 11):
            locator[-1] = locator[-1].replace('%s', str(i))
            ele_list.append(self.wait_get_element_text(locator))
        return ele_list
