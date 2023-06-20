n = int(input("Enter the value of n = "))
count = n*n

while(count >= 1):
    x = count - n + 1
    while(x<=count):
        if(x == count):
            print(x, end='')
        else:
            print(x, end='*')
        x = x + 1
    print()
    count = count - n 