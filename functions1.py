'''
functions/variable are governed by 
LGEB rule for variable scope

L -> local 
G -> Global
E -> Enclosed
B -> Built-in


'''
# try this in idle
# dir()
# num = 100
# dir()

'''
o/p
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
num=100
dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'num']

now num is included
'''

print(dir())
num = 100
print(dir())

print("initially: ",dir())

def t1():
    n = 10
    print("inside the function: ",dir())

t1()

'''
o/p

initially:  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'num']
inside the function:  ['n']
'''

'''
encloser is defined at the last @ 140 line
'''
    

# local variables and global var
# testing for local var
x = 10
def test():
    x = 4
    print(x)

test()
print(x)

'''
the above code will print
4
10
'''

'''
now using global values in function
'''
def test1():
    x = x+1
    print(x)

try:
    test1()
except:
    print(" Trying to access and update global var in function")


'''
the above code will print 
note: with try block
UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
'''

def test2():
    global x
    x = x + 1
    print(x)

test2()


'''
this will give output as 11
'''


#lambda functions

'''
This are unnamed function usually used if the 
block of function body can have not more than 2 lines
'''

# (return of function) = lambda [arguments]  : (set of instructions)

l = lambda sR,eR: [i for i in range(sR,eR+1) if i%2 == 0 ]

print(l(1,10))

'''
the above code will get the list of 
[2, 4, 6, 8, 10]
unnamed functions are called by using the variable assigned
to it and passing arguments to it
'''


# functions with variable length of arguments

def test3(*varArgs):
    for x in varArgs:
        print(x, end=" ")
    return

test3(10,11,12)
print()
test3(1,2,3,4,5)
test3()


'''
the above code will give o/p

10 11 12 -> when 3 parameters
1 2 3 4 5 -> when 5 params
'''


'''
encloser / enclosed variable


'''

gVar = 100
def test4():
    z = 15 
    '''
    here z is enclosed in function test4
    and hence can be accessable to inner function
    as well thatz y z is it is called as encloser
    '''
    print()
    def inner():
        y = 10
        print("y=",y)
        print("inside inner function: ",z)
    inner()
    print("outside function: ",z)
test4()

'''
o/p

y= 10
inside inner function:  15
outside function:  15
'''

# now let try to modify the z in inner

def test5():
    z = 15 
    '''
    here z is enclosed in function test4
    and hence can be accessable to inner function
    as well thatz y z is it is called as encloser
    '''
    print()
    def inner():
        y = 10
        z = z+y
        print("inside inner function: ",z)
    inner()
    print("outside function: ",z)
try:
    test5()
except:
    print("the above code will give o/p as,")
    print("UnboundLocalError: cannot access local variable 'z' where it is not associated with a value")



def test6():
    z = 15 
    '''
    here z is enclosed in function test4
    and hence can be accessable to inner function
    as well thatz y z is it is called as encloser
    '''
    print()
    def inner():
        nonlocal z #make z available to inner to modify
        y = 10
        z = z+y
        print("inside inner function: ",z)
    inner()
    print("outside function: ",z)
test6()

'''
o/p

inside inner function:  25
outside function:  25
'''


'''
finally LGEB is
first it will check if name of var is present
in local then it will move on to global
then check with enclosed and the then go for
built-in variable

'''

g = 10
def test6():
    g = 15
    def inner():
        #g = 20
        print("inner: ",g)
    inner()
    print("outer: ",g)
test6()
print("finally in main: ",g)