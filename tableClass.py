class mulTable:
    __num = 0
    
    def __init__(self):
        self.__num = 0
    
    def getNum(self):
        self.__num = int(input("Enter the Number: "))
    
    def dispMulTab(self):
        for i in range(1,11):
            print(self.__num," x ", i, " = ", (self.__num*i))


m = mulTable()

m.getNum()
m.dispMulTab()