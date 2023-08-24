char = input("enter characters")

if char.isupper():
    print(char.lower())
elif char.islower():
    print(char.upper())
else:
    print("error")