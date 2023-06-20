# def func1(str1="XYZ",str2="ABC"):
#     print("Hi,",str1,str2)
# # try:
# func1(str2=" John")
# # except:
# #     print("Error: func1() missing 1 required positional argument: 'str1'")

# '''
# o/p
# TypeError: func1() missing 1 required positional argument: 'str1'
# '''



# def func1(str1, *varArgs):
#     print(varArgs)
#     print(str1)
#     for i in varArgs:
#         print(i)

# func1(101,"Bhima",35,'M')

'''
def func1(keys1, *varArgs):
    l = []
    l = list(varArgs)
    print(l)

    d = dict()
    d[keys1] = l
    
    print(d)
    
func1(10001,"Bhima",35,'M')
'''

l = [[1,2],[3,4],[5,6]]
print(l[1][1])
l.reverse()
print(l)

'''
1 2 3
4 5 6
7 8 9

1 2 3
7 8 9
4 5 6
'''
