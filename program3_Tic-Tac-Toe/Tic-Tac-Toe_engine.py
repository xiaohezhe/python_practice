import numpy as np

def new_board():
    new_empty_board = [
      [None, None, None],
      [None, None, None],
      [None, None, None]
    ]# lists of lists
    return new_empty_board



board = new_board()
board[0][0] = 'x'
board[0][1] = 'o'
board[0][2] = 'x'

board[1][2] = 'o'
board[2][0] = 'o'
board[2][1] = 'x'
board[2][2] = 'o'




def render(board):
    #change None to ' '
    b= []
    i =0
    for element in board:
        c=[]
        for grid in element:
            if grid is None:
                grid = ' '
            c.append(grid)
        b.append(c)
            
          
    print("  012\n--------") 
    for row1 in b[:]:
        print(str(i)+"|"+''.join(row1)+"|")
        i +=1
    print("--------")


print(render(board))