class Person:
    str2 = "xyz"
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
    def __init__(self):
        print("Init function got executed")
        # func1()
    
    def func1(self, str1):
        print("Hello!, ",str1)


p = Person()
p.func1("Bhima")
print(p.str2)

p2 = Person()
print(p2.str2)

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age) 