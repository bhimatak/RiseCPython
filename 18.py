l = [1,2,3,4,5,6]
rl = []
k = 3
count=0
i =0

while(i<len(l)):
    t = l[count:count+k]
    print(t)
    t.reverse()
    rl += t 
    count += k
    i += k
    print(i)

print(rl)  
# t = l[count:count+k]
# print(t)