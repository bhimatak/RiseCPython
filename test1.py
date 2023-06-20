class test:
    def __init__(self):
        #self.__updateSw()
        print("initiated")
    def publicMth(self):
        print("This is public method")
        self.__updateSw()
    def __updateSw(self):
        print("this is private method")

t = test()
t.publicMth()
t.__updateSw()