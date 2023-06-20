class stackClass:
    
    
    def __init__(self):
        self.l = []
        self.MAXCAP = 5
        self.TOP = 0
        self.BOTTOM = 0


    def pushStk(self,num):
        # global TOP
        # global MAXCAP
        # # print(TOP)
        if self.TOP == self.MAXCAP:
            print("Stack is FULL","\nUnable to insert ", num," in stack")
            return
        self.l.append(num)
        self.TOP = self.TOP + 1

    def popStk(self):
        # global TOP
        # global MAXCAP
        
        if self.TOP == self.BOTTOM:
            print("Stack is Empty")
            return
        print("Poped out ",self.l[self.TOP-1])
        self.l.pop()
        self.TOP = self.TOP - 1

    def dispList(self):
        if not self.l:
            print("Stack is empty")
            return
        print(self.l)

    def display(self):
        while True:
            print("1. Push\n2. Pop\n3. Display. \n4 Exit")
            ch = int(input("Choice : "))
            if ch == 1:
                num = int(input("Enter the Number: "))
                self.pushStk(num)
            elif ch == 2:
                self.popStk()
            elif ch == 3:
                self.dispList()
            elif ch == 4:
                break
            else:
                print("Enter the correct choice")

s = stackClass()
s.display()
