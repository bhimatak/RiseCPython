list1 = [x for x in range(1,11)]
print(list1)
key = 5
mid = 0
l = 0
h = 0
# initially l will be pointing to low/ zeroth position
# high should be length of list 
h = len(list1)-1
# calculate mid
count = 0
flag = 0
while l<=h:
    mid = (l+h)//2
    # print(list1[mid]," mid=",mid)
    if list1[mid]==key:
        flag = 1
        break
    
    elif key > list1[mid]:
        # go for right side of the list
        l = mid+1
        
    elif key < list1[mid]:
        # go for the left side of the list
        h = mid - 1
        
    else:
        pass 

if flag == 1:
    print("found @ {} position".format(mid))
else:
    print("not found")