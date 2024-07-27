"""
# File       : 最小公倍数.py
# Time       ：2024/7/27 11:14
# Author     ：AsuCalyx
# version    ：python 3.7
"""
#编写一个程序，找出能被从1到给定数字n（包括n）的所有数字整除的最小正数
def smallest_multiple(n):
    # 此处写你的代码
    temp = n
    while (True):
        for i in range(1, n + 1):
            if temp % i == 0:
                continue
            else:
                temp += 1
                break
        else:
            break
    return temp


# 输入n
n = int(input())
# 调用函数
print(smallest_multiple(n))