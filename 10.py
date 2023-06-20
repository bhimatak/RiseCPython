# n = int(input())

l = [13,7,6,12]
n =len(l)
big = 0
# for i in range(n):
#     l.append(int(input()))

for i in range(n):
    big = l[i]
    for j in range(i,n):
        if big < l[j]:
            big = l[j]
            break
            
    if i == j:
        print(l[i],"->-1")
    else:        
        print(l[i],"->",big)
    print("\n\n")
    