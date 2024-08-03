"""
# File       : 双基回文数.py
# Time       ：2024/8/3 10:55
# Author     ：AsuCalyx
# version    ：python 3.7
"""
"""
编写一个程序来检查一个数字是否是双基回文数。
回文是指从前往后读和从后往前读都一样的字母、数字的序列。
双基回文数是指在十进制和二进制表示中都是回文的数字。
"""
def check_double_base_palindrome(number):
    # 此处编写代码
    count = 0
    str_number = str(number)
    bin_number = bin(number)[2:]
    if str_number == str_number[::-1]:
        count +=1
    if bin_number == bin_number[::-1]:
        count += 1
    if count == 2:
        return True
    return False

# 获取用户输入
number = int(input())

# 调用函数
print(check_double_base_palindrome(number))