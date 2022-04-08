from xinliUI.utils.get_yaml import get_yaml_data

b=get_yaml_data(r"D:\PythonObjects\xinliUI\common\admin_elements.yaml")["AgentManagementPage"]['many_agent_name']
c = b[-1].replace('%s', str(1))
print(c)