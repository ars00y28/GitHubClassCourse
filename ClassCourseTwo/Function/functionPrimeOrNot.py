def prime(num):
    prime = True
    i = 2
    if num == 1:
        prime = None
    elif num == 2:
        prime = True
    elif num <= 0:
        prime = None
    else:
        while i < num:
            if num % i == 0:
                prime = False
                break
            i = i + 1
    return prime



num = int(input("Please enter a number:"))

if prime(num):
    print(f"{num} is prime")
else:
    print(f"{num} is composite")

reply = input("Want to input again? Press 'n' to exit:")

while reply != 'n':
    
    num = int(input("Please enter a number:"))

    if prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is composite")

    reply = input("Want to input again? Press 'n' to exit:")
        
