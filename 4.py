n = int(input())

# for i in range(n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

for i in range(n,0,-1):
    print("*"*i, end="")
    print()
'''
    *
   * *
  * * *    
 * * * *    
* * * * *
 * * * *
  * * *
   * *
    *
    
'''