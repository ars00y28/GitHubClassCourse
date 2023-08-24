RaceTime =0
RaceHours = int(input("Enter race hours"))
RaceMinutes = int(input("Enter race minutes"))
RaceSeconds = int(input("Enter race seconds"))

RaceTime = (RaceHours *3600)+ (RaceMinutes *60) + RaceSeconds

print("Total Race time",RaceTime)
