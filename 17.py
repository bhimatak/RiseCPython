def plainNum(num):
    str1 = str(num)
    if str1 == str1[::-1]:
        return 1
    else:
        return 0
    
# num = int(input())
l = [121,345]
count = 0
for i in l:
    if plainNum(i) == 1:
        count += 1
if len(l) == count:
    print("palin array")
else:
    print("not a palin array")
