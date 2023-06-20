num = 2
count = 1
# while count<11:
#     #print(str(num)+" x "+ str(count)+ " = "+str(num*count))
#     print("{} x {} = {}".format(num,count,(num*count)))
#     count=count+1

# for count in range(1,11):
#     # print(count)
#     print("{} x {} = {}".format(num,count,(num*count)))

sr = int(input())
er = int(input())
for count in range(sr,er+1):
    if(count%2 == 0):
        print("{} = even".format(count))
    else:
        print("{} = odd".format(count))
print("Thank you")


