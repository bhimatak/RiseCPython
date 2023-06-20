class Node:
    def __init__(self):
        self.val = 0
        self.next = None


n1 = Node()
n2 = Node()
n3 = Node()

print(n1)
print(n2)
print(n3)

n1.val = 10
n2.val = 20
n3.val = 30

# print(n1)
# print(n2)
# print(n3)

n1.next = n2
n2.next = n3

head = n1
temp = head

print("head=",head)
print(temp.val,end="->")
temp = temp.next
print(temp.val,end="->")
temp = temp.next
print(temp.val,end="->")
n4 = Node()
n4.val=40
n3.next = n4
temp = temp.next
print(temp.val,end="->")
n5 = Node()
n5.val = 50
n5.next = head
head = n5
temp = head
print("\nAfter adding in the begining\n")
prevN = head
nextN = head
while temp is not None:
    print(temp.val,end="->")
    temp = temp.next
    
print("getting prev and next values")
prevN = head
nextN = head
count = 0
while nextN is not None:
    print("Iteration: ", (count+1))
    print("Prev: ",prevN.val)
    print("Next: ",nextN.val)
    if (nextN.val == 30):
        break
    prevN = nextN
    nextN = nextN.next
    count+=1

print("Found 30 at: ")
print("Prev: ",prevN.val)
print("Next: ",nextN.val)
prevN.next = nextN.next

print("After deleting 30")
temp = head
while temp is not None:
    print(temp.val,end="->")
    temp = temp.next
    
print("None")

n6 = Node()
n6.val = 100

prevN = head
nextN = head
count = 0
while nextN is not None:
    print("Iteration: ", (count+1))
    print("Prev: ",prevN.val)
    print("Next: ",nextN.val)
    if (nextN.val == 10):
        break
    prevN = nextN
    nextN = nextN.next
    count+=1

print("Found 10 at: ")
print("Prev: ",prevN.val)
print("Next: ",nextN.val)
print("Address Next: ", nextN)
temp = nextN.next
print("Address of temp: ",temp)
print("Value stored in temp: ", temp.val)
print("Address Next to next: ", nextN.next)
nextN.next = n6
n6.next = temp

print("After inserting n6 @ 10")
temp = head
while temp is not None:
    print(temp.val,end="->")
    temp = temp.next
    
print("None")

