import numpy as np
def new_board():
    new_empty_board = [
      [None, None, None],
      [None, None, None],
      [None, None, None]
    ]# lists of lists
    return new_empty_board

# =============================================================================
# Error handling - an edge-case
# =============================================================================
def is_valid_move(board,move_coords):
    #如果玩家输入的数在3*3方格内，且grid为空，则返回true
    if move_coords in [(i,j) for i in range(3) for j in range(3)]:
        if board[move_coords[0]][move_coords[1]] is None:
            return True
        else:
            
            return False
    else:
        
        return False


def render(board):
    #change None to ' '
    rendered_board = ""
    b= []
    i =0
    for element in board:
        c=[]
        for grid in element:
            if grid is None:
                grid = ' '
            c.append(grid)
        b.append(c)
            
          
    rendered_board += "  012\n--------\n"
    for row1 in b[:]:
        rendered_board += str(i)+"|"+''.join(row1)+"|\n"
        i +=1
    rendered_board += "--------\n\n"
    return rendered_board


# print(render(board))


# =============================================================================
# Get player input
# =============================================================================
def get_move():
    x =input("what's your move's X co-ordinate? : ")
    y =input("what's your move's Y co-ordinate? : ")
    #排除异常输入，如果玩家输入无效字符，比如abdsf,防止程序crushed，会给坐标一个（-1，-1）的错误值
    try:
        co_ordinate =(int(x),int(y))
    except Exception:
        co_ordinate = (-1,-1)
    return co_ordinate


# print(move_coords)#mover_coords type is tuple

# =============================================================================
# Execute moves
# =============================================================================




def make_move(board,move_coords,sign):
    i = 0
    j = 0
    
    for element in board:
        if i == move_coords[0]:
            for grid in element:
                if j == move_coords[1]:
                    board[i][j] = sign
                else:
                    j+=1
        else:
            i+=1
    return board
# =============================================================================
# check for winners
# =============================================================================    

def get_winner(board):   
#try to get the measure of fuction'get_winner'
    winner_board = np.array(board)
    #.astype change true or false to 1 or 0
    #if it is 'o' the gird changed to 1 and if it is 'x' the gird changed to -1
    #if it is None, the grid changed to 0
    check_board = (winner_board == 'o').astype(int) - (winner_board == 'x').astype(int)

    #check_vector is (1,1,1)
    check_vector = np.ones((3,1))   
    result1 = check_board@check_vector #转置，行变列，相乘后判断每一行是否有3或-3
    result2 = check_board.transpose()@check_vector#可以判断每一列是否有-3和3
    #[1. 1. 1.]*[[ 1 -1  1] 
     #           [ 0  1  1]
     #           [ 1 -1  1]]
     #trace 是对角线相加
    result3 = np.trace(check_board)
    
    for element1 in result1:
        if element1 == 3 or element1 == -3:
            return True
        
    for element2 in result2:
        if element2 == 3 or element2 == -3:
            return True


    #for element3 in result3:
    if result3 == 3 or result3 == -3:
        return True
    
    return False
        
        
# =============================================================================
# players take alternate moves until the board fills up
# =============================================================================
# while True:
#     move_coords = get_move()
#     print(move_coords)
#     #如果is_valid_move函数返回值为真，则break,否则无效，再输一遍
    
#     if is_valid_move(board,move_coords):
#         break
#     else:
#         print("invalid move, try again!")

# board_update = make_move(board,move_coords,"o")

# past_board = render(board_update)
# print(past_board)

# while True:
#     move_coords1 = get_move()
#     if is_valid_move(board,move_coords1):
#         break
#     else:
#         print("invalid move, try again!")

# board_update1 = make_move(board_update,move_coords1,"x") 
# print(render(board_update1))       

board = new_board()#board type is list 
counter = 0    
while True:
    board_update = board_update1 =""
    while True:
        move_coords = get_move()
        print(move_coords)
        #如果is_valid_move函数返回值为真，则break,否则无效，再输一遍
        
        if is_valid_move(board,move_coords):
            break
        else:
            print("invalid move, try again!")
    
    board_update = make_move(board,move_coords,"o")
    
    past_board = render(board_update)
    counter +=1
    print(past_board)
    if get_winner(board_update):
        winner=0
        break
    if counter == 9:
        winner = -1
        break
    


    while True:
        move_coords1 = get_move()
        if is_valid_move(board,move_coords1):
            break
        else:
            print("invalid move, try again!")
    
    board_update1 = make_move(board_update,move_coords1,"x")
    counter +=1
    print(render(board_update1))
    if get_winner(board_update1):
        winner=1
        break
    
if winner ==0:
    print("o player wins!")
elif winner == 1:
    print("x player wins!")
else:
    print("Draw!")

















