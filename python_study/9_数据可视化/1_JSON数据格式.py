#json是轻量级的数据交换格式，负责不同编程语言中的数据传递，可以按照指定格式去组织和封装数据
#json本质是一个带有特定格式的字符串

import json
data = [{"name":"asuka","age":"18"},{"name":"ayanami","age":"18"},{"name":"真嗣","age":"14"}]
#ensure_ascii 主要用于转换中文,表示不适用ascii码转换而是直接输出
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)
print("****************")

data1 = {"name":"ayanami","age":"18"}
json_str1 = json.dumps(data1)
print(type(json_str1))
print(json_str1)
print("****************")

#将json字符串转换为python数据类型,注意单引号
data2 = '[{"name":"asuka","age":"18"},{"name":"ayanami","age":"18"},{"name":"真嗣","age":"14"}]'
l_data2 = json.loads(data2)
print(type(l_data2))
print(l_data2)
print("****************")

data3 = '{"name":"ayanami","age":"18"}'
l_data3 = json.loads(data3)
print(type(l_data3))
print(l_data3)