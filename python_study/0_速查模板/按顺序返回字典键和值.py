"""
# File       : 按顺序返回字典键和值.py
# Time       ：2024/7/27 11:01
# Author     ：AsuCalyx
# version    ：python 3.7
"""
def get_sorted_keys_values(dict_obj):
    # 此处写你的代码
    sorted_keys = sorted(dict_obj.keys())
    # 创建一个列表，包含按字母顺序排列的键和对应的值
    sorted_key_value_pairs = [(key, dict_obj[key]) for key in sorted_keys]

    # 提取键和值到两个独立的列表
    sorted_keys_list = [item[0] for item in sorted_key_value_pairs]
    sorted_values_list = [item[1] for item in sorted_key_value_pairs]

    # 返回一个由两个列表组成的列表：键和对应的值
    return [sorted_keys_list, sorted_values_list]


# 获取用户输入转为字典
dictionary = eval(input())

# 调用函数
print(get_sorted_keys_values(dictionary))