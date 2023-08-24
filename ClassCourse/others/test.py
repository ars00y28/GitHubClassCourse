HorseName = input("enter your horse name")
Wins = int(input("input number of wins"))
PenaltyWeight = 0

if Wins == 0:
    PenaltyWeight = 0
elif Wins ==1 :
    PenaltyWeight = 4
elif Wins > 1:
    PenaltyWeight = 8

print("your horse"+ " "+HorseName+" "+ "got penalty weight: ",PenaltyWeight, "kg")

