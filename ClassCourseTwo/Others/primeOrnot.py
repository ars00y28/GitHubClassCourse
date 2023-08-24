num = int(input("enter a number: "))

i = 2

prime = True

if num == 1:
    print("Neither Prime Nor Composite")
elif num == 2:
    print("Prime Number")
elif num <= 0:
    print("Not Valid Try again!!!")
else:
    while i < num :
        if num % i == 0 :
            print("not a prime number")
            prime = False
            break
        i = i + 1
    if prime == True:
        print("prime Number")

