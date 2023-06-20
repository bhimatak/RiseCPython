'''
private members of class
'''

class Person:
    __age = 0
    __name = ""
    def __init__(self,age=1,Name="xyz"):
        self.__age = age
        self.__name = Name
    def setAge(self,age):
        self.__age = age
    def setName(self,Name):
        self.__name = Name
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

p = Person()

print(p.getName())
print(p.getAge())

p.__name = "Bhima"
print(p.getName())


'''
the above will not modify the name as it is private
it will remain unchanged as "bhima"
'''

p.setName("Shankar")
p.setAge(23)
print(p.getName())
print(p.getAge())

'''
this will change the values of the obj
'''

'''
arrays of obj
'''
l = []
l.append(Person(23,"Bhima1"))
l.append(Person(24,"Bhima2"))
l.append(Person(25,"Bhima3"))
l.append(Person(26,"Bhima4"))

for x in l:
    print(x.getName(), x.getAge())
