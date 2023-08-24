max = 3
HeadPointer = 0 
TailPointer = -1
noElement = 0

list = [" " for i in range(max)]

def addQueue(newData : str): ### adding value to the queue
    global max, HeadPointer , TailPointer, noElement
    if noElement >= max:
        print('queue is full !!! ')
    else:
        TailPointer = TailPointer + 1
        if TailPointer > max - 1:
            TailPointer = 0 
        list[TailPointer] = newData
        noElement = noElement + 1
    
def removeQueue():
    global max, HeadPointer, TailPointer, noElement
    if noElement <= 0:
        print('List is empty !!!')
    else:
        HeadPointer = HeadPointer + 1
        noElement = noElement - 1
        if HeadPointer > max - 1:
            HeadPointer = 0 

addQueue('apple')
addQueue('orange')
addQueue('banana')

print(list)
removeQueue()
removeQueue()
print(HeadPointer)

addQueue('pineapple')
print(list)