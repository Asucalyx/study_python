def convert_str_list_to_dict(str_list):
    temp = str_list.split()
    dict_temp= {}
    for i in temp:
        key , value = i.split("=")
        dict_temp[key] = value
    return dict_temp

# 输入字符串
str_list = input()

# 调用函数
print(convert_str_list_to_dict(str_list))