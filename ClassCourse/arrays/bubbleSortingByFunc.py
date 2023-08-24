def my_function ():
    temp = 0

for i in range(0,4):
    for j in range(0,4):
        if list[j] > list[j + 1]:
            temp = list[j]
            list[j] = list[j + 1]
            list[j + 1] = temp
        else:
            pass


