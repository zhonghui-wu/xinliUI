from xinliUI.common.base_page import BasePage
from xinliUI.config.config import project_admin_url, admin_phone, login_code
from xinliUI.page_objects.admin_home_page import AdminHomePage
from xinliUI.utils.all_path import admin_elements_yaml_path


class LoginPage(BasePage):

    def open_loginpage(self):
        self.open_url(project_admin_url)
        return self

    def login_admin_sys(self):
        """
        执行登录操作
        :return: 首页
        """
        self.wait_click_element(self.switch_phone_login)
        self.input_text(self.iphone_input, admin_phone)
        self.input_text(self.code_input, login_code)
        self.click_element(self.login_button)
        return AdminHomePage(admin_elements_yaml_path)


if __name__ == '__main__':
    login = LoginPage(admin_elements_yaml_path).open_loginpage()
    login.login_admin_sys().logout_admin_sys()