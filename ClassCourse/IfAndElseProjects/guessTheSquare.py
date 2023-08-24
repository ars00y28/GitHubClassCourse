import random

x =1
while x!=0:
     RandomNumber = random.randint(0, 100)

     print(RandomNumber)
     guess = int(input("square of given number is: "))

     if guess == RandomNumber * RandomNumber:
            print("you are correct!!!!")
     else:
            print("you are wrong try again!!!")
            x = 0