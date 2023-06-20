'''
closers
1. nested functions
2. functions are first class object
'''

def outFunc():
    z = 10
    def inFunc():
        print("inside inFunc",z)
    inFunc()
    print("OutSide outFunc: ",z)

outFunc()

'''
here i can't call inFunc outside the outFunc
if tried it will give me 
NameError: name 'inFunc' is not defined
'''

print(outFunc)
'''
the output will give me
<function outFunc at 0x000002479F1004A0>
it gives the ref of the function where it is located
'''
test1 = outFunc

test1()

'''
test1 is pointing to the same location of outfunc 
hence o/p is same as outFunc
inside inFunc 10
OutSide outFunc:  10
'''

'''
get the ref of the inner function
'''

def o1():
    def in1():
        return 2
    return in1

a = o1()
print(a)

'''
o/p
<function o1.<locals>.in1 at 0x000001F0B398D8A0>

this is the ref of inner function
'''

print(a.__name__)

'''
o/p
in1 -> the name of the inner function
'''

print(a()) # here we are calling inFucn directly and getting the result

# o/p -> 2 -> return(2)

'''
here we are executing the inFunc outside its scope
this technique is called as closer

or 
function object that remembers the
values in the enclosing scope
even if there are not present in the
memory are called closers in python

hence closers should have
1. nested func's
2. nested func's must refer
   values in enclosing scope
3. enclosing func must return nested
   function
   
uses of closers,
1. can avoid global values
2. data hiding
3. implement decorators

'''

'''
decorators
'''

def test2(expr):
    def u1(func):
        def i1():
            return func() + expr
        return i1
    return u1

@test2("Bhima")
def d_test():
    return "Good Morning! "

print(d_test())


def divDecorator(func):
    def inFunc(*args):
        l1 = []
        l1 = args[1:]
        for i in l1:
            if i == 0:
                return "Divide by zero error"
        return func(*args)
    return inFunc

@divDecorator
def d2(a,b):
    return a/b
@divDecorator
def d3(a,b,c):
    return (a/b/c)

print(d3(10,2,0))