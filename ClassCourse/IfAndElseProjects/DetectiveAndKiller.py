import  random

playerOne = input("enter the name of player one: ")
playerTwo = input("enter the name of player two: ")
playerThree = input("enter the name of player three: ")
playerFour = input("enter the name of player four: ")
playerFive = input("enter the name of player five: ")

list = [playerOne,playerTwo,playerThree,playerFour,playerFive]

killer = random.choice(list)


guess = (input("guess the killer "))

if guess == killer:
     print("you have solved the crime detective")
elif guess != killer:
    guess = (input("guess the killer "))
    if guess == killer:
        print("you have solved the crime detective")
    elif guess != killer:
        guess = (input("guess the killer "))
        if guess == killer:
            print("you have solved the crime detective")
        elif guess != killer:
            guess = (input("guess the killer "))
            if guess == killer:
                print("finally you have solved the crime detective")
            elif guess !=killer:
                print(f"you have failed the killer was {killer} now you must die ")



