

def fibonacci(num:int)->int:
    x = 1
    y = 1
    print(1,1,end=",")
    sum = x + y 
    while sum <= num:
        print(sum,end=",")
        x = y 
        y = sum 
        sum = x + y

fibonacci(45) 
    