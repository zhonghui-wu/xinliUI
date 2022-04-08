from xinliUI.common.base_page import BasePage
from xinliUI.page_objects.agent_management_page.agent_managemen_page import AgentManagementPage
from xinliUI.utils.all_path import admin_elements_yaml_path


class AdminHomePage(BasePage):
    """
    管理后台首页跳转到各个页面
    """
    def goto_agent_management_page(self):
        """
        进入代理商管理中的代理商管理页
        :return:
        """
        self.wait_click_element(self.agent_management_button)
        self.wait_click_element(self.agent_management)
        return AgentManagementPage(admin_elements_yaml_path)

    def goto_Agent_staff_management_page(self):
        """
        进入代理商员工管理
        :return:
        """
        self.wait_click_element(self.agent_management_button)
        self.wait_click_element(self.Agent_staff_management)

    def goto_Agent_customer_management_page(self):
        """
        进入代理商客户管理
        :return:
        """
        self.wait_click_element(self.agent_management_button)
        self.wait_click_element(self.Agent_customer_management)

    def goto_Agent_level_management(self):
        """
        进入代理商等级管理
        :return:
        """
        self.wait_click_element(self.agent_management_button)
        self.wait_click_element(self.Agent_level_management)

    def goto_Agent_area_management_page(self):
        """
        进入代理商区域管理
        :return:
        """
        self.wait_click_element(self.agent_management_button)
        self.wait_click_element(self.Agent_area_management)

    def logout_admin_sys(self):
        """
        用于退出登录
        :return:
        """
        self.move_to_element(self.admin_info)
        self.click_element(self.admin_logout)
        self.click_element(self.admin_logout_sure_button)