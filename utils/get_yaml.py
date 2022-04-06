import yaml
from all_path import test_login_data_yaml_path


def get_yaml_data(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    print(get_yaml_data(f"{test_login_data_yaml_path}"))