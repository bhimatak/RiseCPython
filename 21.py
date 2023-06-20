def func1(list1):
    print("Inside Function")
    print(id(list1[0]))
    print(id(list1[1]))
    print(id(list1[2]))
    list1 = [1,2]
    print("Inside function: ",list1)

    print("Inside Function after update")
    print(id(list1[0]))
    print(id(list1[1]))
    print("Inside function: ",list1)

    
l = [5,10,15]
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))
func1(l)
print("outside function", l)
print(id(l[0]))
print(id(l[1]))
print(id(l[2]))
