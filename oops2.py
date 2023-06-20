'''
class variable
'''

class test:
    classVar = "xyz" # class variable belongs to all obj
    
    def __init__(self,name):
        self.name = name
    def testMt(obj1):
        return [obj1.name,obj1.classVar]
    
t = test("Bhima")
print(t.testMt())
    