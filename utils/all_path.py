# -- coding: utf-8 --
# 通过获取当前环境的地址，避免切换环境后path不对的问题
import os


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 举例
test_login_data_yaml_path = os.path.join(project_path, "case_datas\\") + "admin_login_data.yaml"


if __name__ == '__main__':
    print(test_login_data_yaml_path)