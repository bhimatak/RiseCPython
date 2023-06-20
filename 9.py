# list1 = [-4,0,0,3,2,-1]
n = int(input())
l = []
flag = 0
for i in range(n):
    l.append(int(input()))
i = 0
for i in range(n):
    sL = 0
    sR = 0
    
    for j in range(i):
        # print("i=",i,"j=",j,l[j], end=" ")
        sL = sL + l[j]
        # print(sL)
        
    for k in range(i+1,n):
        sR = sR + l[k]
        # print(sR)
    
    if sL == sR:
        flag = 1
        break
    # print("\n\n")

if flag == 1:
    print("pos =",i," value=",l[i])
else:
    print("-1")
    
