from xinliUI.common.base_page import BasePage
from xinliUI.page_objects.agent_management_page.add_agent_page import AddAgentPage
from xinliUI.utils.all_path import admin_elements_yaml_path


class AgentManagementPage(BasePage):
    """
    代理商管理页
    """
    def get_first_agent_name(self):
        """
        获取第一个代理商名称
        :return: 代理商名称
        """
        return self.wait_get_element_text(self.first_agent_name)

    def get_first_agent_number(self):
        """
        获取第一个代理商编号
        :return: 代理商编号
        """
        return self.wait_get_element_text(self.first_agent_number)

    def get_first_higheragent_name(self):
        """
        获取第一个上级代理商名称
        :return: 第一个上级代理商名称
        """
        return self.wait_get_element_text(self.first_higheragent_name)

    def get_first_agent_area(self):
        """
        获取第一个代理区域
        :return: 代理区域名称
        """
        return self.wait_get_element_text(self.first_agent_area)

    def get_first_agent_stats(self):
        """
        获取第一个代理商状态
        :return: 代理商状态
        """
        return self.wait_get_element_text(self.first_agent_stats)

    def agent_number_search(self, text, isreset=False):
        """
        输入代理商编号并搜索,重置
        :param text: 输入代理商编号
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.input_text(self.agent_number_search_input, text)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def agent_name_search(self, text, isreset=False):
        """
        搜索代理商名称
        :param text: 输入代理商名称
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.input_text(self.agent_name_search_input, text)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def agent_phone_search(self, text, isreset=False):
        """
        代理商手机号搜索
        :param text: 输入的代理商手机号
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.input_text(self.phone_search_input, text)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_agent_area_search(self, isreset=False):
        """
        选择第一个代理区域搜索
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.agent_area_search)
        self.click_element(self.first_agent_area_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_first_agent_level_search(self, isreset=False):
        """
        选择第一个代理等级搜索
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.agent_level_search)
        self.click_element(self.first_agent_level_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_havedebt_search(self, isreset=False):
        """
        搜索有欠款的代理商
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.debtState_search)
        self.click_element(self.havedebt_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_notdebt_search(self, isreset=False):
        """
        搜索无欠款的代理商
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.debtState_search)
        self.click_element(self.notdebt_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_normal_search(self, isreset=False):
        """
        搜索正常状态的代理商
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.state_search)
        self.click_element(self.normal_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def to_disabled_search(self, isreset=False):
        """
        搜索被禁用的代理商
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.click_element(self.state_search)
        self.click_element(self.disabled_search)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def higheragent_name_search(self, text, isreset=False):
        """
        上级代理商输入并搜索，重置
        :param text: 上级代理商名称输入
        :param isreset: 判断是否需要重置，默认是需要重置，为Ture就不需要重置
        :return:
        """
        self.input_text(self.higheragent_name_search_input, text)
        self.click_element(self.search_button)
        if not isreset:
            self.click_element(self.reset_button)

    def click_add_agent(self):
        """
        点击添加代理商按钮
        :return:
        """
        self.click_element(self.add_agent_button)
        return AddAgentPage(admin_elements_yaml_path)

    def click_first_agent_check_button(self):
        """
        点击第一个代理商的查看按钮
        :return:
        """
        self.click_element(self.first_agent_check_button)

    def click_first_agent_edit_button(self):
        """
        点击第一个代理商的编辑按钮
        :return:
        """
        self.click_element(self.first_agent_edit_button)

    def click_first_agent_set_products_button(self):
        """
        点击第一个代理商的设置代理产品按钮
        :return:
        """
        self.click_element(self.first_agent_set_products_button)

    def click_first_agent_disabled_button(self):
        """
        点击第一个禁用按钮
        :return:
        """
        self.click_element(self.first_agent_disabled_button)
