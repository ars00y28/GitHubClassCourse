x = 1

while x !=0:
    num = int(input("enter a positive or negative number"))
    if num <0:
        print("negative number")
    elif num >=0:
        print("positive number")
    else:
        x = 0
        print("error")