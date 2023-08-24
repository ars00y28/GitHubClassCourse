HeightInMeter = float(input("enter your height in meters"))
WeightInKilograms = float(input("enter your weight in kilograms"))

x = HeightInMeter*HeightInMeter
bmi = WeightInKilograms/x

print(bmi)

if bmi < 18.5:
    print(f"your bmi is:{bmi} you are underweight")
elif bmi >=18.5 and bmi<=24.4:
    print(f"your bmi is:{bmi}your weight is normal!!!")
elif bmi >=25 and bmi <=29.9:
    print(f"your bmi is:{bmi}you are overweight")
else:
    print(f"your bmi is:{bmi}you are obsese")
