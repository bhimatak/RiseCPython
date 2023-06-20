class Node:
    def __init__(self):
        self.data = 0
        self.nref = None

class cLList:
    
    def __init__(self):
        self.head = None
    
    def addBegin(self, num):
        nn = Node()
        nn.data = num
        if self.head is None:
            print("List is Empty")
            self.head = nn
            nn.nref = self.head
        else:
            print("Adding {} to begining of the list".format(num))
            temp = self.head
            while temp.nref is not self.head:
                temp = temp.nref
            nn.nref = self.head
            temp.nref = nn
            self.head = nn
    
    def addEnd(self,num):
        nn = Node()
        nn.data = num
        if self.head is None:
            self.head = nn
            nn.nref = self.head
        else:
            temp = self.head
            while temp.nref is not self.head:
                temp = temp.nref
            temp.nref = nn
            nn.nref = self.head
            
        
    def delNode(self, Key):
        if self.head is None:
            print("Empty List")
        else:
            if self.head.data == Key:
                if self.head.nref is self.head:
                    print("Deleted {} value".format(head.data))
                    self.head = None
                    return
                else:
                    temp = self.head
                    while temp.nref is not self.head:
                        temp = temp.nref
                    print("Deleted {} value".format(Key))
                    
                    self.head = self.head.nref
                    temp.nref = self.head
            else:
                temp = self.head
                prev = self.head
                flag = 0
                while temp.nref is not self.head:
                    if temp.data == Key:
                        flag = 1
                        break
                    prev = temp
                    temp = temp.nref
                if flag == 0:
                    print("Key {} not found in the list".format(Key))
                else:
                    print("Deleted {} value".format(temp.data))
                    prev.nref = temp.nref
                    
                    
                                    
    def dCList(self):
        last = self.head
        # print("list is")
        # print(last.data,end="->")
        # print(last.nref)
        # print(last)
        while last.nref is not self.head:
            print(last.data,end="->")
            last = last.nref
        print(last.data,end="->")
        print("None")
            
c = cLList()
c.addBegin(30)
c.addBegin(20)
c.addBegin(10)
c.addEnd(40)
c.addEnd(50)

c.dCList()
c.delNode(30)
c.dCList()
c.delNode(10)
c.dCList()

