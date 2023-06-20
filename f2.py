# def test5():
#     z = 15 
#     def inner():
#         nonlocal z
#         y = 10
#         z = z+y
#         print("inside inner function: ",z)
#     inner()
#     print("outside function: ",z)
# test5()


g = 10
def test6():
    #g = 15
    def inner():
        #g = 20
        print("inner: ",g)
    inner()
    print("outer: ",g)
test6()
print("finally in main: ",g)