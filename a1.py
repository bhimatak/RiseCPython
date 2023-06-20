'''
s1 = "listen"
s2 = "slient"

if(sorted(s1) == sorted(s2)):
    print("Yes")
else:
    print("No")
'''
row = 3
num = 1
for i in range(1,row+1):
    for k in range(row-i,0,-1):
        print(" "*k, end="")
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print()
    print()
    