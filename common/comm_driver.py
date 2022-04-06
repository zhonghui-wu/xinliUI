# 写一个通用的浏览器类
from selenium import webdriver
from xinliUI.config.config import headless_set, browname_set, implicitly_time_set


class Singe(object):
    """
    实现单例
    """
    _instance = None  # 定义一个变量来存放实例

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:  # 如果实例为空
            cls._instance = super().__new__(cls)  # 则新建一个实例
        return cls._instance  # 返回一个实例


class CommDriver(Singe):
    driver = None

    def get_driver(self, headless=headless_set, browname=browname_set, implicitly_time=implicitly_time_set):
        """
        通用的浏览器类
        :param headless: 默认为有头
        :param browname: 默认为chrome
        :param implicitly_time: 默认为5s
        :return: 返回一个浏览器
        """
        if self.driver is None:
            if not headless:
                if browname == 'chrome':
                    self.driver = webdriver.Chrome()
                elif browname == 'firefox':
                    self.driver = webdriver.Firefox()
                else:
                    raise Exception(f'{browname} is not supported')

            else:
                if browname == 'chrome':
                    self.option = webdriver.ChromeOptions()
                    self.option.add_argument('-headless')
                    self.driver = webdriver.Chrome(options=self.option)
                elif browname == 'firefox':
                    self.option = webdriver.ChromeOptions()
                    self.option.add_argument('-headless')
                    self.driver = webdriver.Firefox(options=self.option)
                else:
                    raise Exception(f'{browname} is not supported')
                self.driver.implicitly_wait(implicitly_time)
                self.driver.set_window_size(1920, 1080)
        return self.driver


if __name__ == '__main__':
    driver = CommDriver().get_driver()
    driver.get('https://admin.xinli.callwine.net/')
    driver.get('https://www.baidu.com')