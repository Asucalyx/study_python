# 字符串拼接
print("はじめ" + "ましで")
name1 = "hello"
name2 = "world"
name3 = 13
name4 = 2.66
name5 = 14
print(name1 + "my" + name2)
# 字符串格式化
print("%s my %s" % (name1, name2))
print("%d my %7.1f" % (name3, name4))
# f format，快速格式化，但是不会进行精度控制和理会格式
print(f"{name3} my {name4}")
print("---------------")
# 表达式
print("13+14=%d" % (name3 + name5))
print("字符串的数据类型是%s" % type("nihao"))
print("******************************")
# 小练习
company_name = "SpaceX"
stock_price = 19.99
stock_code = "003032"
stock_Price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司名：{company_name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日增长系数是：%.1f，经过%d天的增长后，股价达到了：%.2f" % (
    stock_Price_daily_growth_factor, growth_days, stock_price * stock_Price_daily_growth_factor ** growth_days))
