"""
# File       : 最大公约数.py
# Time       ：2024/7/22 10:23
# Author     ：AsuCalyx
# version    ：python 3.7
"""
def find_gcd(a, b):
    # 在此处编写代码
    while b:
        a, b = b, a % b
    return a


# 输入整数
first_number = int(input())
second_number = int(input())
# 调用函数
print(find_gcd(first_number, second_number))