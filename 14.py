l = list()

def pNumbers(sR,eR):
    countE = 0
    countO = int((sR+eR)/2)
    for i in range(sR,eR+1):
        if i%2 == 0:
            print(i," = even")
            l.insert(countE,i)
            countE += 1
        else:
            print(i," = odd")
            l.insert(countO,i)
            countO += 1
            
    
pNumbers(33,56)
print(l)
