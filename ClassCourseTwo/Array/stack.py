max = 8
list = [ " " for i in range(max)]


TopPointer = - 1 ### -1 represents that the stack is empty !!!

def push(NewData : str):    ### creating a function to 'push' data in the stack.  
    global TopPointer  ### 'global' keyword is necessary here because the function thinks 'topPointer' is a local variable.
    if TopPointer + 1  >= max:
        print(f"Stack overflow maximum capacity of the stack is {max}")
    else:
        TopPointer = TopPointer + 1
        list[TopPointer] = NewData


def pop(): #### creating a function to 'pop' or remove data from  the stack.
    global TopPointer
    if TopPointer < 0:
        print("stack underflow, The stack is empty!!! ")
    else:
        print(list[TopPointer])
        TopPointer = TopPointer - 1
