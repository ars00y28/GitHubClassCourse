import random
sides = ['left', 'right', 'middle']
x = 0
gk = random.choice(sides)
shooting = input("Which side do you want to shoot? left, right or middle? ")
while x<=0:
    if shooting == gk:
        print("Penalty Saved!")
        x = 1
    else:
        print("Penalty Scored!")
        x = 1