def zhu_cai_dan(name):
    print("-------------主菜单----------------")
    print(f"{name}您好，请输入数字选择操作：")
    print("查询余额 [输入1]\n"
          "存款 [输入2]\n"
          "取款 [输入3]\n"
          "退出 [输入4]\n")
    user_in = int(input("请输入:"))
    if user_in == 1:
        cha_xun(money)
    elif user_in == 2:
        cun_kuan()
    elif user_in == 3:
        qu_kuan()
    else:
        tui_chu()


def cha_xun(money):
    print(f"您的账户余额为:{money}")


def cun_kuan():
    global money
    cun_money = int(input("请输入存款数:"))
    money += cun_money
    print(f"您的余额为{money}")


def qu_kuan():
    global money
    print(f"当前余额为{money}")
    qu_money = int(input("请输入取款数:"))
    money -= qu_money
    print(f"您的余额为{money}")


def tui_chu():
    exit()


money = 0
name = input("请输入姓名:")
while True:
    zhu_cai_dan(name)
