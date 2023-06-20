# n = int(input())

# for i in range(n,0,-1):
#     print(" "*i, end="")
#     print()

# for i in range(1,n+1,1):
#     print("* "*i,end="")
#     print()

n = int(input())
count = 1

while(count <= n):
    print("* "*count)
    count = count+1
    
count = n-1
while(count >= 1):
    print("* "*count)
    count = count - 1