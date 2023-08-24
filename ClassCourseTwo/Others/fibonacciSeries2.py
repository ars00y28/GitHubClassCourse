def fibonacci(num):
    x = 1
    y = 1
    sum = x + y 
    print(x)
    print(y)
    while sum < num:
        print(sum)
        x = y 
        y = sum 
        sum = x + y 
        


print(fibonacci(21))