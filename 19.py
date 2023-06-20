l = [1,2,3,4,5,6,7,8]

n = len(l)
k = 1

count = 0
i=0
rL = []
while i<n:
    t = l[count:count+k]
    # print(t)
    t.reverse()
    rL += t
    count+=k
    i += k
    
print(rL)
# t = l[count:count+k]
# print(t)
