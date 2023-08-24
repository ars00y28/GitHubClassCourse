#### we are going to create a chess board using 2d array!!!!

#### chess board is 8*8 square with 32 white and 32 black squares

#### we are going to denote white squares with # and black squares with * signs....


board = []

for i in range(8):
    row = []
    for j in range(8):
        if (i+j) % 2 == 0:
            row.append("#")
        else:
            row.append("*")
    board.append(row)


##### trace table ######

##  i  j  i+j  position(i + j % 2 == 2)   
##  0  0   0            True                      
##  0  1   1            False                     
##  0  2   2            True                      
##  0  3   3            False                      
##  0  4   4            True
##  0  5   5            False
##  0  6   6            True
##  0  7   7            False
##  0  8   8            True
##  1  0   1            False ## second row started here
##  1  1   2            True
##  1  2   3            False
##  1  3   4            True
