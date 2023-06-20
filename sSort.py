l = [3,5,2,6,1,8]
min = l[0]

def findMin(list1,i):
    min = list1[i]
    count = 0
    for j in range(i,len(list1)):
        # if min < list1[j]:
        #     min = list[j]
        #     count = j
        print(list1[j])
    return count

j = findMin(l,0)

print("j=",j)
# for i in range(len(l)):
    
#     # print(l[i])
#     for j in range(len(l)):
#         if min > l[j]:
#             min = l[j]
    
# print(min)
