l = []
MAXCAP = 5
TOP = 0
BOTTOM = 0


def pushStk(num):
    global TOP
    global MAXCAP
    # print(TOP)
    if TOP == MAXCAP:
        print("Stack is FULL","\nUnable to insert ", num," in stack")
        return
    l.append(num)
    TOP = TOP + 1

def popStk():
    global TOP
    global MAXCAP
    
    if TOP == BOTTOM:
        print("Stack is Empty")
        return
    print("Poped out ",l[TOP-1])
    l.pop()
    TOP = TOP - 1

def dispList():
    if not l:
        print("Stack is empty")
        return
    print(l)

def display():
    while True:
        print("1. Push\n2. Pop\n3. Display. \n4 Exit")
        ch = int(input("Choice : "))
        if ch == 1:
            num = int(input("Enter the Number: "))
            pushStk(num)
        elif ch == 2:
            popStk()
        elif ch == 3:
            dispList()
        elif ch == 4:
            break
        else:
            print("Enter the correct choice")


display()
