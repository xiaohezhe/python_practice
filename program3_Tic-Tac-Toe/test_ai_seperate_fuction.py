import numpy as np
import random
board = [
  [None, None, 'X'],
  [None, None, 'X'],
  [None, None, None]
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
def random_ai(board, player):
    legal_moves = []
    for row,element in enumerate(board):
        for ind,etc in enumerate(element):
            if etc is None:
                legal_moves.append((row,ind))
    print(legal_moves)    
    board_coordinate = random.choice(legal_moves)#select the element of a list randomly
    return board_coordinate
  
print (random_ai(board, 'X'))
