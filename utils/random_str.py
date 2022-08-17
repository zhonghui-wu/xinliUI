from random import sample
from string import digits, ascii_letters


def get_random_str(length):
    """
    当添加名称的时候使用，避免重复
    :param length: 需要的位数
    :return:
    """
    return ''.join(sample(ascii_letters+digits, length))


if __name__ == '__main__':
    print(get_random_str(10))