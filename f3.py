# def outFunc():
#     z = 10
#     def inFunc(x):
#         print("inside inFunc",x)
#     inFunc(202)
#     print("OutSide outFunc: ",z)
#     return inFunc

# t = outFunc()
# print(t.__name__)
# t(101)

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
'''

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

print(d2(0,10))