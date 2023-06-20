class Myclass:
    pass

p = Myclass

print(p)
'''
<class '__main__.Myclass'>
'''

'''
class NameOfClass:
    members
    methods
    
1.
The __init__() Function
its a builtin func 
all the class have this init method which is always executed
when the class is initiated
use of init func is to initialize the values 
to the object
properties
or the other operation to do when 
the object is being created

'''

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 

'''
o/p
John
36
'''

'''
2. 
The __str__() Function

The __str__() function controls what should be returned when the class object is represented as a string.

If the __str__() function is not set, the string representation of the object is returned:

'''

class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person1("John", 36)

print(p1) 

'''
o/p
John(36)
'''


'''
Object Methods

Objects can also contain methods. Methods in objects are functions that belong to the object.

Let us create a method in the Person class:
Example

Insert a function that prints a greeting, and execute it on the p1 object:
'''
class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc() 

'''
The self Parameter

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

'''

class Person3:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name+" age= "+str(abc.age))

p1 = Person3("John", 36)
p1.myfunc() 

# access or modify the object value
p1.age = 20
p1.myfunc() 

del p1
try:
    print(p1.myfunc())
except:
    print("Will give the output as")
    print("NameError: name 'p1' is not defined. Did you mean: 'p'?")