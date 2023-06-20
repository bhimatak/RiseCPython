'''
private methods=> defined by __ => 2 underscores
'''

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

'''
o/p
this is private method -> this is called imm when the obj is created
This is public method -> this is called by user
'''

'''
we can't call __updateSw as publicMth using obj
as it os private to the class
only methods within the class can access it
'''
try:
    t.__updateSw()
except:
    print("AttributeError: 'test' object has no attribute '__updateSw'")

