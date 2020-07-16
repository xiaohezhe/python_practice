import numpy as np
import random
board = [
  ['x','o', None],
  [None, None, 'x'],
  [None, None,'o' ]
]
# def random_ai

# =============================================================================
# We’re going to start by writing one of the simplest AIs possible. 
# This AI will look at the board, find all the legal moves,
# and return one of them at random
# =============================================================================
# To find the index of a 2D list
# =============================================================================
# # for row,element in enumerate(board):
# #     for ind,etc in enumerate(element):
# #         print((row,ind))
# =============================================================================
# def random_ai(board, player):
#     legal_moves = []
#     for row,element in enumerate(board):
#         for ind,etc in enumerate(element):
#             if etc is None:
#                 legal_moves.append((row,ind))
#     print(legal_moves)    
#     board_coordinate = random.choice(legal_moves)#select the element of a list randomly
#     return board_coordinate
  
# print (random_ai(board, 'X'))

# =============================================================================
# AI that makes winning moves
# =============================================================================
def finds_winning_moves_ai(board,player):
    winner_board = np.array(board)
    print(winner_board)
    #.astype change true or false to 1 or 0
    #if it is 'o' the gird changed to 1 and if it is 'x' the gird changed to -1
    #if it is None, the grid changed to 0
    check_board = (winner_board == 'o').astype(int) - (winner_board == 'x').astype(int)
    print(check_board)
    #check_vector is (1,1,1)
    check_vector = np.ones((3,1))   
    result1 = check_board@check_vector #转置，行变列，相乘后判断每一行是否有3或-3
    result2 = check_board.transpose()@check_vector#可以判断每一列是否有-3和3
    #trace 是对角线相加
    result3 = np.trace(check_board)

    
    legal_moves = []
    legal_moves1 = []
    if player == 'x':
        if ((result3 == -2) | np.any(np.array(result2) == -2)| np.any(np.array(result1) == -2 )):
            if result3 == -2:
                if check_board[0][0] == 0:
                    new_board_coordinate = (0,0)
                elif check_board[1][1] == 0:
                    new_board_coordinate = (1,1)
                elif check_board[2][2] == 0:
                    new_board_coordinate = (2,2)
            else:
                for a,b in enumerate(result1):
                    if b == -2:# 'x' player
                        for c,d in enumerate(check_board[a]):
                            if d ==0:
                                new_board_coordinate =((a,c))
                
                
                for a,b in enumerate(result2):
                    if b == -2:# 'x' player
                        for c,d in enumerate(check_board.transpose()[a]):
                            if d ==0:
                                new_board_coordinate =((c,a))
        else:
    
                    
            for row,element in enumerate(board):
                for ind,etc in enumerate(element):
                    if etc is None:
                        legal_moves.append((row,ind))    
            new_board_coordinate = random.choice(legal_moves)
                
    
    elif player =='o':
        if ((result3 == 2) | np.any(np.array(result2) == 2)| np.any(np.array(result1) == 2 )):
            if result3 == 2:
                if check_board[0][0] == 0:
                    new_board_coordinate = (0,0)
                elif check_board[1][1] == 0:
                    new_board_coordinate = (1,1)
                elif check_board[2][2] == 0:
                    new_board_coordinate = (2,2)
            else:
                for a,b in enumerate(result1):
                    if b == 2:# 'x' player
                        for c,d in enumerate(check_board[a]):
                            if d ==0:
                                new_board_coordinate =((a,c))
                
                
                for a,b in enumerate(result2):
                    if b == 2:# 'x' player
                        for c,d in enumerate(check_board.transpose()[a]):
                            if d ==0:
                                new_board_coordinate =((c,a))
        else:
    
                    
            for row,element in enumerate(board):
                for ind,etc in enumerate(element):
                    if etc is None:
                        legal_moves.append((row,ind))    
            new_board_coordinate = random.choice(legal_moves)               
                
                
    return new_board_coordinate

print (finds_winning_moves_ai(board, 'o'))
print (finds_winning_moves_ai(board, 'o'))