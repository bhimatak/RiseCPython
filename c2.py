class Person:
    name = ""
    age = 0
    
    def __init__(self, Name,Age):
        self.name = Name
        self.age = Age
    
    def setAge(self,Age):
        self.age = Age
        
    def setName(self, Name):
        self.name = Name
    
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def dispDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        
    def getDetails(self):
        self.name=input("Enter Name: ")
        self.age = int(input("Enter Age: ")) 


p1 = Person("Bhima",45)
p1.dispDetails()
print(p1.getAge())

p2 = Person("",0)
p2.getDetails()
p2.dispDetails()
