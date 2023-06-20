class Node:
    
    def __init__(self,num):
        self.data = num
        self.next = None

class LL():
    
    def __init__(self):
        self.head = None
    def insertBegin(self,nData):
        nn = Node(nData)
        if self.head is None:
            self.head = nn
        else:
            last = self.head
            nn.next = last
            self.head = nn
            
    def insertNode(self,nData):
        nn = Node(nData)
        
        if self.head is None:
            self.head = nn
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = nn
    
    def delNode(self,key):
        if self.head is None:
            print("List is empty")
            return
        nextN = self.head
        prevN = self.head
        while nextN is not None:
            if nextN.data == key:
                # print("found")
                break
            prevN = nextN
            nextN = nextN.next
            
        if nextN is None:
            print("Key Not Found")
            return
        
        # if key is at the begining
        if prevN == nextN:
            self.head = nextN.next
        
        # print(prevN.data, nextN.data)
        prevN.next = nextN.next
    
    def pop(self):
        
        if self.head is None:
            print("Empty List")
            return
        nextN = self.head
        prevN = self.head
        while nextN.next is not None:
            prevN = nextN
            nextN = nextN.next
        # print("prev ele",prevN.data)
        # print("Popped out ",nextN.data)
        if prevN == nextN:
            # print("First")
            self.head = None
            return
        prevN.next = None
        del nextN 
        
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        last = self.head
        
        while last is not None:
            print(last.data,end="->")
            last = last.next
        print("None")
        


n = LL()

n.insertNode(10)
n.insertNode(20)
n.insertBegin(100)
n.insertNode(30)
n.insertBegin(200)
n.insertBegin(300)
n.display()
# n.delNode(20)
n.pop()
n.display()
n.pop()
n.display()
n.pop()
n.display()
n.pop()
n.display()
n.pop()
n.display()
n.pop()
n.display()
n.pop()
n.display()


