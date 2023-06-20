class Node:
    
    def __init__(self, num):
        self.data = num
        self.next = None
        self.prev = None

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

print(n1)
print(n2)
print(n3)

# forward direction
n1.next = n2
n2.next = n3

# backward direction
n2.prev = n1
n3.prev = n2
'''
head = n1

print("head->", head)

print("prevAdd {} - address {} - nextAdd {} = value {} \
    ".format(head.prev,head,head.next,head.data))

head = head.next
print("prevAdd {} - address {} - nextAdd {} = value {} \
    ".format(head.prev,head,head.next,head.data))

head = head.next
print("prevAdd {} - address {} - nextAdd {} = value {} \
    ".format(head.prev,head,head.next,head.data))

head = head.next
'''

head = n1
while head.next is not None:
    # print("prevAdd {} - address {} - nextAdd {} = value {} \
    # ".format(head.prev,head,head.next,head.data))
    print(head.data, end="->")
    head = head.next
print(head.data, end="->")
print("None")
print(head.prev)

while head.prev is not None:
    print(head.data, end="->")
    head = head.prev
print(head.data, end="->")
print("None")
