"""
    open(name,mode,encoding) 打开函数
    name:要打开的文件名(可以包含文件所在的具体路径)
    mode:打开文件的模式
        r:只读模式，文件指针放在开头
        w:写入模式，删除原有内容，如果文件不存在则创建新文件
        a:追加模式，新内容将被写在原内容后，如果文件不存在则创建新文件
    encodeing：编码格式(推荐UTF-8)
"""
open("D:\GitHub\study_python\python学习")