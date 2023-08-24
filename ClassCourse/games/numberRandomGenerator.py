import random

RandomNumber = random.randint(0,100)

if RandomNumber%1 == 0:
   GamePhase=  input('enter y for starting the game!!!')
   if GamePhase == 'y':
       print("game has started")
       GuessedNum = int(input("guess the number: "))
       if GuessedNum == RandomNumber:

           print('the number was',RandomNumber)
           print("congrats you have guessed the number!!!!!")

       elif GuessedNum < RandomNumber:
           print('the number was', RandomNumber)
           print("you guessed less try again!!!")

       elif GuessedNum > RandomNumber:
           print('the number was', RandomNumber)
           print("you guessed more try again!!!")

   else:
       print(("game has ended refresh again if you want to play"))