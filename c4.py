class Person:
    __age = 0
    name = ""
    def __init__(self,age=1,Name="xyz"):
        self.__age = age
        self.name = Name
    def setAge(self,age):
        self.__age = age
    def setName(self,Name):
        self.name = Name
    def getName(self):
        return self.name
    def getAge(self):
        return self.__age

p = Person()

print(p.getName())
print(p.getAge())

p.name = "Bhima"
print(p.getName())
p.setName("Bhima")
print(p.getName())