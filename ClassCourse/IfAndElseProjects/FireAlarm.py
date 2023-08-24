trigger = False
threshold = 90.0

temperature = float(input("enter the temperature"))

if temperature >= threshold:
    trigger = True
    print(f"the state of fire alarm is on: {trigger}")
else:
    print(f"the state of fire alarm is on: {trigger}")