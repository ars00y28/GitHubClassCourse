
def Counter():
    file = open('essay.txt','r')
    count = 0  
    spaceCondition = False
    for temp in file:
        j=0
        while temp[j] == ' ':
            j += 1  
        length = len(temp)
        
        for i in range(j,length):
            c = temp[i]
            if c != ' ':
                spaceCondition = False
            elif spaceCondition == False and c == ' ':
                spaceCondition = True
                count += 1

    file.close()
    return count

print(Counter())

