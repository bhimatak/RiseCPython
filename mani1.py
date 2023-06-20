# str1 ="problemsone"
# n = 3

str1 ="edbaaodnn"
n = 4


flagh=1
flagd=0
counth=0
countd=0
l1 = []
l2 = []
l3 = []
for i in str1:
    # print(i, end=" ")
    if counth == n:
        counth = 0
        flagd = 1
        flagh = 0
       
        print()
   
    if countd == int(n/2):
        countd = 0
        flagh = 1
        flagd = 0
        print()
       
    if flagh == 1:
        print("h: ",i,end=" ")
        l1.append(i)
        counth += 1
   
    if flagd == 1:
        print("d: ",i,end=" ")
        l2.append(i)
        countd += 1
    print("flagh: ",flagh,"\tflagd: ",flagd)


print(l1)
lh =[]
j = 0
for i in l1:
    if j<len(l1):
        rowh= l1[j:j+n]
        lh.append(rowh)
        j += n
       
print(lh)
   

ld =[]
j = 0
for i in l2:
    if j<len(l2):
        rowd= l2[j:j+int(n/2)]
        ld.append(rowd)
        j += int(n/2)
       
print(ld)


str2 = ""
count=0

print(len(lh))
# print(lh[0][0])
# print(lh[0][1])
# print(lh[0][2])
# print(lh[0][3])
# print(lh[1][0])

count=0
print(lh)
# for i in range(len(lh)+1):
#     for j in range(len(lh)+1):
#         print(lh[i][j])
#     # str2 += i[count][count]
#     # count+=1

# print(str2)

s1 = [["a","b","c","d"],["e","f","g"]]
lens1 = len(s1)
# print(s1[0].count())
print(s1)

print("loop")

# for i in range(len(s1)):
#     s1[i].reverse()
# print(s1)
l5 = []
for i in range(len(s1)):
    # print(len(s1[i]))
    l5.append(len(s1[i]))
# print(max(l5))
max1  = max(l5)
stt = []
for i in range(len(s1)):
    # print(s1[i].index(s1[i][-1]))
    slen = s1[i].index(s1[i][-1])
    for j in range(max1):
        if j<=slen:
            print(s1[i][j], end=" ")
            stt.append(s1[i][j])
        else:
            # print("empty")
            stt.append(" ")
        # print(s1[i][j])
    print()
    # for j in range(len(s1[i])):
    #     print(s1[i][j])   
# s2 = s1[lens1-1]
# print(s2)

# print(l2)
print(stt)
'''
stt1 = ""
count1 = len(stt)
stt1 += stt[0:max1-0].pop()
# print(stt[0:max1].pop())
# print(stt[0:max1-1].pop())
# print(stt[0:max1-2].pop())

# print("Jello: ",stt[max1:count1-1].pop())

stt1 += stt[max1:count1].pop()
print(stt1)

stt1=""
count1 -= 1
stt1 += stt[0:max1-1].pop()
stt1 += stt[max1:count1].pop()
print(stt1)

stt1=""
count1 -= 1
stt1 += stt[0:max1-2].pop()
stt1 += stt[max1:count1].pop()
print(stt1)
'''
stt1 = ""
count1 = len(stt)


for i in range(len(stt)+1):
    stt1=""
    # count1 -= 1
    # stt1 += stt[0:max1-i].pop()
    # stt1 += 
    print("max: ",max1,"count: ",count1-i)
    print(stt[max1:count1-i].pop())
    print(stt1)

    
    

# stt1=""
# count1-=1
# stt1 += stt[1:max1].pop()
# stt1 += stt[max1:count1].pop()
# print(stt1)



# for i in range(max1):
    