list = [10,40,30,20]


temp = 0

for i in range(0,3):
    for j in range(0,3):
        if list[j] < list[j + 1]:  
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp



print(f"this is the largest number in this list {list[0]}")
print(f"this is the smallest number in this list {list[3]}")


