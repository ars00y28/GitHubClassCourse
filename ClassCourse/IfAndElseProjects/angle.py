angle = float(input("enter the angle"))

if angle == 90:
    print("right angle ")
elif angle <90 and angle >0:
    print("acute angle")
elif angle >90 and angle<180:
    print ("obtuse angle ")
elif angle > 180 and angle <360:
    print("reflex angle")
else:
    pass