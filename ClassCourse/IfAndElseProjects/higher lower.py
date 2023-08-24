import random

RanNum = random.randint(0, 100)


guess = int(input("guess the number"))
x = 1
while x != 0:
    if guess == RanNum:
        print("congrats you have guessed the number!!!!")
        x = 0
    elif guess < RanNum:
        print("you guessed low")
        guess = int(input("guess the number"))
    elif guess > RanNum:
        print("you guessed high")
        guess = int(input("guess the number"))
    else:
        pass