"""
# File       : 不重复元素的列表.py
# Time       ：2024/8/3 10:39
# Author     ：AsuCalyx
# version    ：python 3.7
"""
"""
定义函数find_unique()，它接受一个列表作为参数。
在函数内部，找出列表中只出现一次的数字。
以列表中的出现的顺序返回唯一的数字
"""
def find_unique(lst):
    # 此处编写代码
    temp_dict = {}
    for i in lst:
        temp_dict[i] = temp_dict.get(i,0) + 1
    temp_list = [i for i,count in temp_dict.items() if count == 1]
    return temp_list



# 获取用户输入并转为数字列表
numbers = list(map(int, input().split()))

# 调用函数
print(find_unique(numbers))