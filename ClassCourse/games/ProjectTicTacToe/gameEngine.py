import board  as b
import os
os.system("clear")

b._drawBoard_()



x = 0

while x < 10: #### total turns === 9 thus the turns alternate from X to O.
    x += 1
    
    marker = ''
    if x % 2 == 0: ### if x is divisible by 2 then player O will get turn...
        marker = 'O'
    else:
        marker = 'X' ### if x is not divisible by 2 then player X will get turn...

    row = int(input(f"enter the row player {marker} [0-2]: "))  #### entering the row of placement.
    coln = int(input(f"enter the column player {marker} [0-2]: ")) #### entering the column of placement.
    
    if b.board[row][coln] =='#': #### is board[row][coloum] = # then only their can be a placement it is done so value cannot be given in same place twice.
        b.board[row][coln] = marker ### x or o depending 
        os.system("clear")
        b._drawBoard_()
    else:
        print("This cell is occupied!!!! choose another one")
        x -= 1 #### subtracting value of x by 1 so game goes step back to the player who made a mistake.
        

                ###### Winning Conditions ########################
    if b.board[0][0] == b.board[0][1] == b.board[0][2] == marker:
        print(f"player {marker} wins the game!!!!")
    
    elif b.board[0][0] == b.board[1][0] == b.board[2][0] == marker:
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[0][1] == b.board[1][1] == b.board[2][1] == marker :
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[0][2] == b.board[1][2] == b.board[2][2] == marker:
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[1][0] == b.board[1][1] == b.board[1][2] == marker:
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[2][0] == b.board[2][1] == b.board[2][2] == marker:
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[0][0] == b.board[1][1] == b.board[2][2] == marker:
        print(f"player {marker} wins the game!!!")
        break

    elif b.board[0][2] == b.board[1][1] == b.board[2][0] == marker:
        print(f"player {marker} wins the game!!!")
        break
    ##### somehow the value of x exceeded for emergency!!!!! #######
    if x > 10:
        break