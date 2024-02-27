import random

money = 10000
for human_code in range(1, 21):
    human_work = random.randint(1, 10)
    if money == 0:
        break
    if human_work < 5:
        print(f"员工{human_code}，绩效低于5，不发工资，下一位")
        continue
    else:
        money -= 1000
        print(f"向员工{human_code}发放工资1000元，账户余额剩余{money}")
print("工资发放完毕")
