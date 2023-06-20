lines = ""
with open('testTxt.txt') as f:
    lines = str(f.readlines())
    count = 1
    f1 = 0
    
    while True:
        print("count=",count)
        if not lines:
            break
        else:
            if count == 1:
                lines = lines[f1:]
            else:
                lines = lines[f1:count]
            print("\n\n")
            print("result: ",lines)
            f1 = lines.find("Question",count)
            print(f1)
            count = count + f1
            
        # f1 = lines.find("Question",count)
        # count = f1
        # lines = lines[count:f1]
        
    # f = lines.find("Question",count)
    # print(lines[count:f])
    
            

#print(lines)