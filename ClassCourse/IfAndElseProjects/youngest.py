ageOne = int(input("enter the first age"))
ageTwo = int(input("enter the second age"))
ageThree = int(input("enter the third age"))
ageFour = int(input("enter the fourth age"))

if ageOne <ageTwo and ageOne <ageThree and ageOne <ageFour:
    print(ageOne," years is the youngest")
elif ageTwo <ageOne and ageTwo <ageThree and ageTwo <ageFour:
    print(ageTwo,"years is the youngest")
elif ageThree <ageOne and ageThree <ageTwo and ageThree <ageFour:
    print(ageThree,"years is the youngest")
else:
    print(ageFour,"years is the youngest")