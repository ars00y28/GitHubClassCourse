
x = int(input('enter a number '))

reverse = 0 
y = 0
cond = True


while x > 0: # 123  = True  12 = True

    reverse = int(reverse*10 + x % 10) # reverse =  3  reverse = 32
    x = int(x/10) # x = 12 x = 1
    print(f"x is {x} and reverse is {reverse}")
    

print(reverse)


