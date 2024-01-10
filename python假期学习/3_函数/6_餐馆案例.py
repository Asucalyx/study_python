def zhu_cai_dan():
    print("-------------主菜单----------------")
    print("asuka您好，请输入数字选择操作：")
    print("查询余额 [输入1]\n"
          "存款 [输入2]\n"
          "取款 [输入3]\n"
          "退出 [输入4]\n")
    user_in=int(input("请输入:"))
    if user_in==1:
        cha_xun()
    elif user_in==2:
        cun_kuan()
    elif user_in==3:
        qu_kuan()
    else:
        break
def cha_xun():
    print(f"您的账户余额为:{money}")
    
