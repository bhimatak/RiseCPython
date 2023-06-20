l = []
MAXCAP = 5
RARE = 0
FRONT = 0


def queue(num):
    global RARE
    global MAXCAP
    # print(TOP)
    if RARE == MAXCAP:
        print("Queue is FULL","\nUnable to queue ", num," in queue")
        return
    l.append(num)
    RARE = RARE + 1

def dequeue():
    global FRONT
    global RARE
    global MAXCAP
    
    if FRONT == RARE:
        print("Queue is Empty")
        return
    
    print("dequeued out ",l[0])
    l.reverse()
    l.pop()
    l.reverse()
    FRONT = FRONT + 1
    

def dispList():
    if not l:
        print("Queue is empty")
        return
    print(l)

def display():
    while True:
        print("1. Queue\n2. Dequeue\n3. Display. \n4 Exit")
        ch = int(input("Choice : "))
        if ch == 1:
            num = int(input("Enter the Number: "))
            queue(num)
        elif ch == 2:
            dequeue()
        elif ch == 3:
            dispList()
        elif ch == 4:
            break
        else:
            print("Enter the correct choice")


display()
