def factorial(num:int)->int:
    x = 1
    y = 1
    for x in range(1,num+1):
        y = x * y 
    return y 

y = factorial(5)
print(y)



def print_main_menu():
    print("*********HELLO PEOPLE***************")
    print("Choose your option!")
    print("1.Play a game")
    print("2. Open facebook")


print_main_menu()