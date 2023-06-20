expStk = []
str1 = "1 2 3 4 + * * 28 / 1 -"
ops = "+-*/%"
# print(str1.split())
l1 = list(str1.split())
# print(l)

l = []
MAXCAP = 50
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
    # print("Poped out x",l[TOP-1])
    # print("Poped out y",l[TOP-2])
    # l.pop()
    # TOP = TOP - 2

def calcExp(x,y,op):
    if op == "+":
        return (x+y)
    elif op == "-":
        return (x-y)
    elif op == "*":
        return (x*y)
    elif op == "/":
        return (x/y)
    elif op == "%":
        return (x%y)
    else:
        return

def dispList():
    if not l:
        print("Stack is empty")
        return
    print(l)


count =0
flag = 0

for i in l1:
    if i in ops:
        # print(i)
        flag = 1
        # do the pop operation
        popStk()
        # x = l[TOP-1]
        # y = l[TOP-2]
        if l:
            x = l.pop()
        if l:
            y = l.pop()
        print("Popped two elements ",x,y)
        ret = calcExp(x,y,i)
        TOP -= 2
        pushStk(ret)
        TOP += 1
    else:
        pushStk(int(i))
        count += 1

print(l)