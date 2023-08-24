list = [300,200,100,400,600,500]

x = 0 
temp = 0 
j = 0 


for x in range(1,6):  ### x is increasing from 1 to 6.
    temp = list[x]  ### the value in the 2nd  part of the list is being backed up. 
    j = x - 1    ### j right now is one part below x. 
    while j >= 0 and list[j] > temp: ### if list[j] > temp then code below will happen. 
        list[j + 1] = list[j]
        j = j - 1
    list[j + 1] = temp


print(list)



#### x|temp| j |
#### 1| 200| 0 | 
####
####
####
####
####
