"""
# File       : Harshad 数.py
# Time       ：2024/8/3 10:15
# Author     ：AsuCalyx
# version    ：python 3.7
"""
"""
如果一个数字可以被它的数字之和整除，那么它就是一个Harshad数，如171：
number = 171
1 + 7 + 1 = 9 [数字之和]
9 正好整除 171
"""
def is_harshad(num):
    # 在此处编写你的代码
    temp = []
    re = num
    while(num != 0):
        tnum = num % 10
        num = num // 10
        temp.append(tnum)
    tnum1 = sum(temp)
    if re % tnum1 == 0:
        return True
    return False

# 获取用户输入
num = int(input())

# 显示输出
print(is_harshad(num))