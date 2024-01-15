# 位置参数 函数根据定义的参数位置来传递参数
"""  def temp(name,age,gender) temp("asuka",18,"w") """
# 关键字参数 可以和位置参数混用，但是位置参数必须在最前面
""" def temp(name,age,gender) temp(age = 18,gender = "w,name = "asuka") """

# 缺省参数 有一个参数时默认的已经写好的，不输入的话就使用默认值 默认值必须统一在最后
""" def temp(name,age,gender = ”w“) temp(age = 18,name = "asuka") """

# 位置不定长参数 不确定要传入多少个参数
""" def temp(*args) args标记为元组"""
# 关键字不定长参数 按照字典传入
""" def temp(**args) args标记为字典"""
