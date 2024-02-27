"""
    open(name,mode,encoding) 打开函数
    name:要打开的文件名(可以包含文件所在的具体路径)
    mode:打开文件的模式
        r:只读模式，文件指针放在开头
        w:写入模式，删除原有内容，如果文件不存在则创建新文件
        a:追加模式，新内容将被写在原内容后，如果文件不存在则创建新文件
    encodeing:编码格式(推荐UTF-8)
"""
f = open("D:/GitHub/study_python/python_study/7_测试文件夹/1_测试","r",encoding="UTF-8")
print(type(f))

print("****************************")
# read()方法 文件对象.read(num) num表示需要读取的数据长度(字节)，未输入则代表全部读取
#多次调用相同文件对象的读取方法，将接着读取上一次的位置
f_read = f.read()
print(f_read)
print("-------------")
#readlines()方法 读取文件的全部行，封装到列表中
f_readlines = f.readlines()
#注释上面的读取操作，重置文件指针
print(f_readlines)
print("-------------")
#readline()方法 读取文件的一行
f_readline = f.readline()
#注释上面的读取操作，重置文件指针
print(f_readline)
print("-------------")
#for循环读取文件内容
#注释上面的读取操作，重置文件指针
for f_line in f:
    print(f_line)

print("**************")
#close()方法 关闭文件对象
f.close()
print("*************")
#with open语法 操作完后可以关闭文件防止忘记close()
with open("D:/GitHub/study_python/python_study/7_测试文件夹/1_测试","r",encoding="UTF-8") as f:
    f.read()
