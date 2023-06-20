with open('testTxt.txt') as f:
    line = None
    d = dict()
    while True:
        line = f.readline()
        # print(line,end="")
        if "Question" in line:
            break
            
    # line = f.readline()
    # print(line,end="")
    if "Question" in line:
        print("Question Found")
        d['Question'] = ""
    line = f.readline()
    # print(line,end="")
    if "\n" == line:
        print("yes")
    else:
        print("No")
    line = f.readline()
    # print(line,end="")
    if "cpp\n" == line:
        print("yes")
    else:
        print("No")
    line = f.readline()
    # print(line,end="")
    if "Copy code\n" == line:
        print("Copy Yes")
    else:
        print("Copy No")
    lines = f.readlines()
    print(lines)
    str1 = ""
    l = ""
    for l in lines:
        if "a)" in l:
            break
        str1 += l
        # print(l,end="")
        # d["Question"] = d["Question"] + l
    
    #print(str1)
    r1 = "".join(lines)
    # print("Result---:", r1, len(r1))
    r1 = r1[len(str1):]
    l2 = r1.split("\n")
    for i in l2:
        s = i.split()
        print(s[1])
    
    f.close()