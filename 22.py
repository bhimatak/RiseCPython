#program to find palindrome
'''
a = lambda num: [ int(str(num)[::-1])==num]

print(a(121))
'''
def isPrime(num):
    # If given number is greater than 1
    flag = 1
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                flag = 0
                break
    else:
        return 0
    if flag == 0:
        return 0
    else:
        return 1

is_prime = lambda number: all( number%i != 0 for i in range(2, int(number**.5)+1) )
for i in range(2,10):
    if(is_prime(i)):
        print(i)    