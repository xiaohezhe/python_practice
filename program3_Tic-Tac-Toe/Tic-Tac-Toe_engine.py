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


board = new_board()#board type is list

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
    print(past_board)
    


    while True:
        move_coords1 = get_move()
        if is_valid_move(board,move_coords1):
            break
        else:
            print("invalid move, try again!")
    
    board_update1 = make_move(board_update,move_coords1,"x") 
    print(render(board_update1))
    
# =============================================================================
# check for winners
# =============================================================================    
    
    


    

    



















