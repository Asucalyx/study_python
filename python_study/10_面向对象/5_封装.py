#封装 = 外部世界事物 ->程序世界事物
#私有变量和方法 以__开头
class Phone:
    __current_voltage = 0
    def __keep_single_core(self):
        print("CPU单核")

    def call_by_5G(self):
        if self.__current_voltage >= 1:
            print("可以")
        else:
            self.__keep_single_core()
            print("不可以")

phone = Phone()
#类对象无法直接调用私有变量和成员方法
# print(phone.__current_voltage)
# phone.__keep_single_core()
phone.call_by_5G()
