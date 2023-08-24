import random

Rnum = random.randint(0,100)

LoseCondition = True

while LoseCondition:
    x = int(input('Guess a number: '))
    if x == Rnum:
        LoseCondition = False
        print('Congratulations You have guessed the Number!!!')
    elif x < Rnum:
        print('you Guessed Less Try again ')
    elif x > Rnum:
        print('you Guessed More Try again')

