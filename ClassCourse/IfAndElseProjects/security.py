print("set the code between 1000 to 9999")

SetCode = int(input("set your  code "))

if SetCode > 9999 or SetCode < 1000:
    print("error")
else:
    pass

TryCode = int(input("enter the code"))

if TryCode == SetCode:
    print("access allowed")
else:
    print("access denied")