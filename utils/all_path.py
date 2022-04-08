# -- coding: utf-8 --
# 通过获取当前环境的地址，避免切换环境后path不对的问题
import os


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 举例
screenshots_path = os.path.join(project_path, "outputs\\screenshots\\")
log_save_path = os.path.join(project_path, "outputs\\logs\\")
admin_elements_yaml_path = os.path.join(project_path, "common\\") + "admin_elements.yaml"


if __name__ == '__main__':
    print(admin_elements_yaml_path)