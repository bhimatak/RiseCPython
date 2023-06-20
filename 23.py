def func1(n):
    if n == 10:
        return
    print("Hello", end=" ")
    
    n += 1
    func1(n)
    print(n)

func1(1)