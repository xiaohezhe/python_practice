import numpy as np

def new_board():
    new_empty_board = [
      [None, None, None],
      [None, None, None],
      [None, None, None]
    ]# lists of lists
    return new_empty_board



board = new_board()
i =0
j =0

print(board[i][j])
board[0][0] = 'o'
board[0][1] = 'x'
board[0][2] = 'o'

board[1][1] = 'o'

board[1][2] = 'o'
board[2][0] = 'o'
board[2][1] = 'x'
board[2][2] = 'o'

#try to get the measure of fuction'get_winner'
winner_board = np.array(board)
print(winner_board)
#.astype change true or false to 1 or 0
#if it is 'o' the gird changed to 1 and if it is 'x' the gird changed to -1
#if it is None, the grid changed to 0
check_board = (winner_board == 'o').astype(int) - (winner_board == 'x').astype(int)
print(check_board)


print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#check_vector is (1,1,1)
check_vector = np.ones((3))
print(check_vector)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

result1 = check_board@check_vector.transpose() #转置，行变列，相乘后判断每一行是否有3或-3
print(result1)
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")

result2 = check_vector@check_board#可以判断每一列是否有-3和3
#[1. 1. 1.]*[[ 1 -1  1] 
 #           [ 0  1  1]
 #           [ 1 -1  1]]
print(result2)

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#trace 是对角线相加
result3 = np.trace(check_board)
print(result3)