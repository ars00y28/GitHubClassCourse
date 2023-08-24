list =  [40,20,10,30,50]




temp = 0

for i in range(0,4):
    for j in range(0,4-i):
        if list[j] > list[j + 1]: 
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
        else:
            pass

print(f"list after sorting: {list}")