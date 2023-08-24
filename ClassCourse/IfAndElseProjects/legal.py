age = int(input("enter your age"))

if age <18:
    print("you are underage for driving")
    print("you are underage for voting")
    print("you are underage for alcohol")
elif age >=18 and age < 21:
    print("you are old enough for driving")
    print("you are old enough for voting")
    print("you are old enough for drinking alcohol")
elif age >=21:
    print("you are old enough for marriage")
    print("you are old enough for driving big vechicles")
else:
    pass
