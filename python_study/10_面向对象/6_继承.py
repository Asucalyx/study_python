"""
# File       : 6_继承.py
# Time       ：2024/3/15 20:50
# Author     ：AsuCalyx
# version    ：python 3.7
"""
"""
    单继承语法：
        class 类名(父类名):
                类内容体
    多继承语法：
        class 类名(父类名1，父类名2， ···· 父类名N):
                类内容体
    多个父类中，如果有同名的成员，默认以继承顺序(从左到右)为优先级
    即:先继承的保留，后继承的被覆盖
"""
class Phone:
    IMEI = None
    producer = "EVA"

    def call_by_4g(self):
        print("4g通话")

class New_Phone(Phone):
    face_id = "2024"

    def call_by_5g(self):
        print("2024新功能")

phone = New_Phone()
print(phone.producer)
phone.call_by_5g()
phone.call_by_4g()

print("****************")
#多继承
class NFCRead:
    nfc_type = "五代"
    producer = "EVA"

    def nfc_read_card(self):
        print("NFC读卡")

    def nfc_write_card(self):
        print("NFC写卡")


class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("开启红外")

class MyPhone(Phone,NFCRead,RemoteControl):
    #补全语法
    pass

my_phone = MyPhone()
my_phone.nfc_read_card()
my_phone.nfc_write_card()
my_phone.control()