from array import *
ThisArray = array('i',[20,50,10,60,80,90,150,100,250,200])
sum = 0
for index in range(len(ThisArray)):
    print(ThisArray[index])
    sum += ThisArray[index]


print('sum :', sum)