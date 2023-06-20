'''
class test:
    def __init__(self):
        print("Initiated")
    
    def module1(self):
        print("module 1")
    
    def module2(self):
        print("module 2")
        
    def module3(self):
        print("module 3")
    
    def choice(self):
        print("1. for module 1")
        print("2. for module 2")
        print("3. for module 3")
        ch = int(input("Choice: "))
        
        if ch == 1: 
            self.module1()
        elif ch == 2:
            self.module2()
        elif ch == 3:
            self.module3()
        else:
            print("Enter correct input") 
        
t = test()

t.choice()
'''

class test:
    def __init__(self):
        print("Initiated")
    
    def module1(self):
        print("module 1")
        l = [1,2,3]
        return l
        
t = test()

ret = t.module1()
print(ret)