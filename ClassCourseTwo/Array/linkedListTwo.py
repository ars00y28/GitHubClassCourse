item = []
head = -1
counter = 0
temp = 0 



def addingVal(data,add = -1):
    global head, counter, prev_add
    item.append([data,add])
    counter = counter + 1


def add(data):
    global head, counter , temp
    if head == -1:
        addingVal(data)
        head += 1
    else:
        if data > item[head][0]:
            temp = head  ### temp == 0
            head = counter  ### head == 1
            addingVal(data,item[temp][1]) ### counter == 2
            item[temp][1] = head
        elif data < item[head][0]:
            item[temp][1] = counter 
            addingVal(data,head)
            head = counter - 1
        else:
            pass




            



add('Bikram')
add('Finzo')
add("Jeeyan")
add("Dinesh")

print(item)


