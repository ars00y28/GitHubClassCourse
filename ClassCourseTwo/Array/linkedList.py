head = 3 
list_size = 4
inmax = 3
next_free_loc = 5 

item = [['ram',-1],['hari',2],['keshav',4],['anil',1],['prem',0],[' ',' '],[' ',' ']]
#print(testItem)

#item = [[' 'for i in range(inmax)] for j in range(list_size)]


def linked():
    print(item[head][0])
    next = item[head][1]
    while next != -1:
        print(item[next][0])
        next = item[next][1]


def find(nam):
    next_item = item[head][0]
    if next_item == nam:
        return head
    next_add = item[head][1]
    while next != -1:
        next_item = item[next_add][0]
        if next_item == nam:
            return next_add
            break
        next_add = item[next_add][1]
    return -1



linked()