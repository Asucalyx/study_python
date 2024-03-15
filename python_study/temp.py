#这是测试py文件，可以在此测试代码
class phone:
    __is_5g_enable = False
    def __check_5g(self,check):
        if check == True:
            print("yes")
        else:
            print("No")
    def call_by_5g(self):
        self.__check_5g(self.__is_5g_enable)
        print("calling")
phone = phone()
phone.call_by_5g()