"""
# File       : 斐波那契数列.py
# Time       ：2024/7/27 10:19
# Author     ：AsuCalyx
# version    ：python 3.7
"""
#递归法 递归是实现斐波那契数列最直观的方法，但效率不是最高的，因为它会重复计算很多项。
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 使用递归方法获取第10项
print(fibonacci_recursive(10))

#动态规划法 动态规划可以存储已经计算过的项，避免重复计算，提高效率。
def fibonacci_dp(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


# 使用动态规划方法获取第10项
print(fibonacci_dp(10))

#空间优化的动态规划 这种方法只存储前两个计算过的项，进一步减少空间复杂度。
def fibonacci_optimized(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# 使用空间优化的动态规划方法获取第10项
print(fibonacci_optimized(10))