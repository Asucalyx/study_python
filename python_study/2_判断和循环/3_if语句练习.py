# 猜数游戏
import random

num = random.randint(1, 10)
guess1 = int(input("请输入猜测数："))
if num == guess1:
    print("恭喜你猜中了")
elif num > guess1:
    print("小了")
    guess2 = int(input("请再猜一次："))
    if num == guess2:
        print("恭喜你猜中了")
    else:
        print(f"你猜错了，答案为{num}")
elif num < guess1:
    print("大了")
    guess3 = int(input("请再猜一次："))
    if num == guess3:
        print("恭喜你猜中了")
    else:
        print(f"你猜错了，答案为{num}")
