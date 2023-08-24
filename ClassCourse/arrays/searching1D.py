list = [10,30,20,50,60,40]


search = int(input('enter the number you want to search for in the list: '))


for x in range(0,5):
    if list[x] == search:
        print(f"value in the list at position {x}")
    else:
        print(f"value not in the list at position {x}")

##### x ==> 0 
#####  list[0] == lets say 20 gives no!!!
####  else statement prints with list[0]
#### x ===> 1 and so on
    

