age1 = 30
if age1 >= 20:
    print("yes")
print("欢迎来到游乐园")
age2 = int(input("请输入年龄："))
if age2 >= 18:
    print("您以成年，需要补票")
elif age2 > 0 & age2 < 18:
    print("你未成年，free")
else:
    print("error")
print("祝你游玩愉快")
