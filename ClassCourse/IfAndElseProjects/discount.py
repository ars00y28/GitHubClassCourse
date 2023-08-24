price = float(input("enter the price"))
dicount = 0

if price >=1000 and price <5000:
    discount = (10/100)*price
    print(f"you get discount{discount}rupees")
elif price >=5000 and price <10000:
    discount = (15/100)*price
    print(f"you get discount{discount}rupees")
elif price >=10000:
    discount = (30/100)*price
    print(f"you get discount{discount}rupees")
else:
    print("you get no discount ")