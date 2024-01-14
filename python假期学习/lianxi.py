def missing_numbers_info(num_list):
    # 此处写下你的代码
    res = []
    sum = 0
    temp = 0
    min1 = min(num_list)
    for i in range(min(num_list), max(num_list)):
        if i in num_list:
            continue
        else:
            temp += 1
            sum += i
    res.append(temp)
    res.append(sum)
    return tuple(res)


# 获取整数输入并将其转换为列表
num_list = list(map(int, input().split()))
# 调用函数
print(missing_numbers_info(num_list))



