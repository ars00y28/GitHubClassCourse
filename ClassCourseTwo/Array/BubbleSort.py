numArr = [5,2,1,3,4]


print(numArr)
x = len(numArr) - 1
for i in range(0,x):
    for j in range(0,x-i):
        if numArr[j] > numArr[j+1]:
            temp = numArr[j]
            numArr[j] = numArr[j+1]
            numArr[j+1] = temp

print(numArr)
