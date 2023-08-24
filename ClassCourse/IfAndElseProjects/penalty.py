NoOfWins = int(input("enter number of your wins"))
penalty = 0

if NoOfWins == 0:
    penalty = 0
    print(f"your penalty weight is:{penalty}kg")
elif NoOfWins >0 and NoOfWins <=2:
    penalty = 2
    print(f"your penalty weight is: {penalty}kg")
elif NoOfWins >2 and NoOfWins <=5:
    penalty = 5
    print(f"your penalty weight is: {penalty}kg")
elif NoOfWins >5:
    penalty = 7
    print(f"your penalty weight is: {penalty}kg")
else:
    print("error")
