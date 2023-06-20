# creating a node class
class Node:
    def __init__(self):
        self.data = 0
        self.next = None

class LList:
    def __init__(self):
        self.head = None
    
    def NewNode(self, value):
        nn = Node()
        nn.data = value
        # print(nn)
        # print(nn.data)
        
        if self.head is None:
            # print("Head was null")
            self.head = nn
            self.head.next = self.head
        else:
            temp = self.head
            
            while temp.next is not self.head:
                temp = temp.next
            temp.next = nn
            nn.next = self.head
    
    def NNBeg(self, num):
        nn = Node()
        nn.data = num
        temp = self.head
        self.head = nn
        nn.next = temp
    
    def delNode(self,num):
        if self.head is None:
            print("Empty List")
            return
        prevN = self.head
        nextN = self.head
        
        
        while nextN is not None:
            if nextN.data == num:
                break
            prevN = nextN
            nextN = nextN.next
        prevN.next = nextN.next
    
    def dispMenu(self):
        while True:
            print("1. Add Node to the End of List")
            print("2. Add Node to Begining of List")
            print("3. Delete a Node in the List")
            print("4. Display Linked List")
            print("5. Exit")
            ch = int(input("Choice: "))
            
            if ch == 1:
                num = int(input("Enter the Number: "))
                self.NewNode(num)
            elif ch == 2:
                num = int(input("Enter the Number: "))
                self.NNBeg(num)
            elif ch == 3:
                num = int(input("Enter the Number: "))
                self.delNode(num)
            elif ch == 4:
                self.dispList()
            elif ch == 5:
                break
            else:
                print("Enter the correct choice")
        
    
    def dispList(self):
        if self.head is None:
            print("Empty List")
            return
        temp = self.head
        if self.head == temp.next:
            print(temp.data,end="->")
                
        else:
            while temp is not self.head:
                # print("Node Address: {} \tNext Address: {} \tValue: {}".format(temp,temp.next,temp.data),end="->")
                # print()
                print(temp.data,end="->")
                temp = temp.next
            
        print("None")

l1 = LList()

# print(l1)
# l1.NewNode(101)
# l1.NewNode(102)
# l1.NewNode(103)
# l1.NewNode(104)
# l1.NewNode(105)
# l1.NNBeg(110)
# l1.dispList()
# l1.delNode(103)
# l1.NNBeg(110)
# l1.dispList()

l1.dispMenu()