import time
numLine = 30
time_s =0.001
for i in range(1,numLine+1):
    no_of_spaces = numLine-i
    no_of_aster = i*2 - 1
    for j in range(no_of_spaces):
        print("A ",end="")
        time.sleep(time_s)
    for k in range(no_of_aster):
        print("b ",end="")
        time.sleep(time_s)
    for l in range(no_of_spaces):
        print("? ",end="")
        time.sleep(time_s)
    print()