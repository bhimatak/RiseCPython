n = int(input())
l = []

for i in range(n):
    l.append(int(input()))
big = l[n-1]
print(big,end=" ")

for i in range(n-1,0,-1):
    if l[i] > big:
        big = l[i]
        print(big, end=" ")
    
    