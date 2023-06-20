class Node:
    def __init__(self):
        self.data = 0
        self.next = None
        self.prev = None

class DLList:
    
    def __init__(self):
        self.head = None
    
    def appendNode(self, num):
        nn = Node()
        nn.data = num
        
        if self.head is None:
            self.head = nn
        else:
            last = self.head
            
            while last.next is not None:
                last = last.next
            last.next = nn
            nn.prev = last
    
    def AddNodeBeg(self, num):
        nn = Node()
        nn.data = num
        temp = self.head
        self.head = nn
        nn.next = temp
        temp.prev = nn
        
    def delNodeKey(self,num):
        if self.head is None:
            print("Empty List")
            return
        
        if self.head.next is None:
            if self.head.data == num:
                self.head = None
                print("Deleted the only Node")
            else:
                print("Key={} not found in the List".format(num)) 
            return
        if self.head.data == num:
            self.head = self.head.next
            self.head.prev = None
            return
        
        nextN = self.head
        
        while nextN is not None:
            if nextN.data == num:
                break
            nextN = nextN.next
        
        if nextN.next is not None:
            nextN.next.prev = nextN.prev
            nextN.prev.next = nextN.next
        else:
            if nextN.data == num:
                nextN.prev.next = None
            else:
                print("Key={} not found in the List".format(num))

    def dispDListF(self):
        if self.head is None:
            print("Empty List")
            return
        last = self.head
        while last is not None:
            print(last.data,end="->")
            last = last.next
        
        print("None")
        
    def dispDListB(self):
        if self.head is None:
            print("Empty List")
            return
        last = self.head
        
        while last.next is not None:
            last = last.next
        
        while last is not None:
            print(last.data, end="->")
            last = last.prev
        print("None")


DLL = DLList()
DLL.appendNode(10)
DLL.appendNode(20)
DLL.AddNodeBeg(5)
DLL.appendNode(30)



DLL.dispDListF() 
DLL.dispDListB()                
DLL.delNodeKey(20)        
DLL.dispDListF() 
DLL.dispDListB()                

