items = []
Head = -1
current_size = 0

def add_item(data,next_addr=-1):
    global current_size
    items.append([data,next_addr])
    current_size += 1

def add_data_correct_loc(data):
    global current_size,Head
    if Head==-1:
        add_item(data)
        Head = current_size-1
    else:
        if data < items[Head][0]: #Data to be put before head item
            temp = Head
            Head = current_size
            add_item(data,temp)
        else:
            next_data = items[Head][0]
            next_addr = items[Head][1]
            prev_index = Head
            inserted = False
            while next_addr != -1:
                prev_addr = next_addr
                next_data = items[prev_addr][0]
                next_addr = items[prev_addr][1]
                if data < next_data:
                    temp = items[prev_index][1]
                    items[prev_index][1] = current_size
                    add_item(data,temp)
                    inserted = True
                    break
                prev_index = prev_addr
            
            #if item not in middle but at the end
            if not inserted:
                items[prev_index][1] = current_size
                add_item(data)
    print_items()
    traverse()
        
def print_items():
    print(f"Head:{Head}")
    index = "Index"
    item = "Data_item"
    add = "Next_Address"
    print(f"{index} {item} {add}")
    for i,item in enumerate(items):
        print(f"{i:<5} {items[i][0]:9} {items[i][1]:<12}")

def traverse():
    next_data = items[Head][0]
    next_addr = items[Head][1]
    print(next_data,end=" ")
    while next_addr != -1:
        next_data = items[next_addr][0]
        next_addr = items[next_addr][1]
        print(next_data,end = " ")
    print()






