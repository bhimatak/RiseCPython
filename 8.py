n = int(input())

for i in range(1,(n*n)+1):
   
    if(i%n == 0):
        print(i, end="")
        print()
    else:
        print(i, end="*")
        
'''
Sample Input:
4
Sample Output:
13*14*15*16
9*10*11*12
5*6*7*8
1*2*3*4

'''
