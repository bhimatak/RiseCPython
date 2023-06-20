class test:
    __a = 0
    __b = 0
    def __init__(self):
        self.a=10
        self.__b=20
        self.__c=30
    def disp(self):
        print(self.__a,self.__b,self.__c,self.a)

t = test()
t.disp()