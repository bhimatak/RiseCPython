a,b = map(int, input().split())
print("Enter + for addition")
print("Enter - for subtraction")
print("Enter * for multiplication")
print("ENter / for division")
print("Choice:", end=" ")
op = input()

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
else:
    print("Wrong input of the operator")

print("Thank you")
