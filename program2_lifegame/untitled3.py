import numpy as np
import random
# # =============================================================================
# # 2-D grids
# # =============================================================================
# # board_state = [
# #     [1,1,1,1,1,1,1],
# #     [1,1,1,1,1,1,1],
# #     [1,1,1,1,1,1,1],
# #     [1,1,1,1,1,1,1],
# #     [1,0,1,1,1,1,1],
# #     [1,1,1,1,1,1,1]
# # ]
# # print(board_state)


# # =============================================================================
# # for loop to create 2-D array
# # =============================================================================
# # def dead_state(width,height):
# #     dead_state = []
# #     for i in range (height):
# #         dead_state.append([])
# #         for j in range (width):
# #             dead_state[i].append(0)
# #     return dead_state



# # =============================================================================
# # an easier way to create 2-D array with random number
# # =============================================================================
# def random_state(width,height):
#     # create array with 0
#     # dead_state = [[0]*width for i in range(height)]
#     # create array with random number
#     dead_state = [[random.random() for i in range(width)] for j in range(height)]
#     return dead_state

# # =============================================================================

   
# width = 3
# height = 3

# array = random_state(width, height)
# # change the list to array
# dimensional = np.array(array)
# print(dimensional)
# shape = dimensional.shape
# print(shape)

# # =============================================================================
# # change the element in the array to 0/1--dead/live
# # =============================================================================
# def cell_state_fuction(width,height):
#     cell_state = []
#     cell_sate_value = 0
    
#     for k in range (shape[0]):
#         cell_state.append([])
#         for p in range (shape[1]):
#             if dimensional[k][p] >= 0.5:
#                 cell_sate_value = 0
#             else:
#                 cell_sate_value = 1
#             cell_state[k].append(cell_sate_value)
# #matrix and can use shape in the later next_board_state fuction
#     dimensional_cell_state = np.array(cell_state)
#     return dimensional_cell_state

# array_cell_state = cell_state_fuction(width, height) 
# print(array_cell_state)



# # =============================================================================
# # change the element in the array using characters whatever i like   
# # =============================================================================

# def render_fuction(width,height):
#     cell_state = []
#     cell_sate_value = 0
    
#     for k in range (shape[0]):
#         for p in range (shape[1]):
#             if dimensional[k][p] >= 0.5:
#                 cell_sate_value = "@"
#             else:
#                 cell_sate_value = "#"
#             cell_state.append(cell_sate_value)
#         cell_state.append("\n") #output one line and change to the next line
#     return cell_state

# array_cell_state_render = render_fuction(width, height) 
#print(array_cell_state_render)# a list

# str = ""
# print(str.join(array_cell_state_render)) #list changes to string

# =============================================================================
# Calculate the next state of the board
# array_cell_state is initial_state
# =============================================================================


# initial_state = array_cell_state



init_state_05 = [
    [0,1,0,1],
    [1,1,1,0],
    [1,0,0,0],
    [1,1,1,1]
]
initial_state =  np.array(init_state_05)
#create new state to store the new value
new_state =[]

a=b=c=d=e=f=g=h=live_total=new_state_value = 0
init_state_shape = initial_state.shape


for y in range(init_state_shape[0]):
    for x in range(init_state_shape[1]):
        # one cell around by 8 neighbors
        if 0<y<(init_state_shape[0]-1) and 0<x<(init_state_shape[1]-1):
            a = initial_state[y-1][x-1]
            b = initial_state[y-1][x]
            c = initial_state[y-1][x+1]
            d = initial_state[y][x-1]
            e = initial_state[y][x+1]
            f = initial_state[y+1][x-1]
            g = initial_state[y+1][x]
            h = initial_state[y+1][x+1]
            live_total = a+b+c+d+e+f+g+h
        # upleft corner cell around by 3 neighbors
        elif x==0 and y==0:
            e = initial_state[y][x+1]
            g = initial_state[y+1][x]
            h = initial_state[y+1][x+1]
            live_total = e+g+h
       
        # upright corner cell around by 3 neighbors
        elif y==0 and x==(init_state_shape[1]-1):
            d = initial_state[y][x-1]
            f = initial_state[y+1][x-1]
            g = initial_state[y+1][x]
            live_total = d+f+g
      
        # bottomleft corner cell around by 3 neighbors
        elif y ==(init_state_shape[0]-1) and x == 0:
            b = initial_state[y-1][x]
            c = initial_state[y-1][x+1]
            e = initial_state[y][x+1]
            live_total = b+c+e               
        
        # bottomright corner cell around by 3 neighbors    
        elif y ==(init_state_shape[0]-1) and x ==(init_state_shape[1]-1):
            a = initial_state[y-1][x-1]
            b = initial_state[y-1][x]
            d = initial_state[y][x-1]
            live_total = a+b+d
      
        # up line cells arounded by 5 neighbors
        elif y==0 and 0<x<(init_state_shape[1]-1):
            d = initial_state[y][x-1]
            e = initial_state[y][x+1]
            f = initial_state[y+1][x-1]
            g = initial_state[y+1][x]
            h = initial_state[y+1][x+1]
            live_total = d+e+f+g+h
        # bottom line cells arounded by 5 neighbors
        elif y==(init_state_shape[0]-1) and  0<x<(init_state_shape[1]-1):
            a = initial_state[y-1][x-1]
            b = initial_state[y-1][x]
            c = initial_state[y-1][x+1]
            d = initial_state[y][x-1]
            e = initial_state[y][x+1]
            live_total = a+b+c+d+e
         #left line cells arounded by 5 neighbors
        elif x == 0 and 0<y<(init_state_shape[0]-1):
           b = initial_state[y-1][x]
           c = initial_state[y-1][x+1]
           e = initial_state[y][x+1]
           g = initial_state[y+1][x]
           h = initial_state[y+1][x+1]
           live_total = b+c+e+g+h
          #right line cells arounded by 5 neighbors
        elif x == (init_state_shape[1]-1) and 0<y<(init_state_shape[0]-1):
           a = initial_state[y-1][x-1]
           b = initial_state[y-1][x]
           d = initial_state[y][x-1]
           f = initial_state[y+1][x-1]
           g = initial_state[y+1][x]
           live_total = a+b+d+f+g
        new_state.append(live_total)
  

dimensional_new_state = np.array(new_state)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(dimensional_new_state.reshape(height,width))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

kill = ((dimensional_new_state<=1)|(dimensional_new_state >3))#live_total为3的变为1， 其他为0
#kill = kill.astype(int)# not kill is 2, 3
print((~(kill)).astype(int))
revive = (dimensional_new_state==3)
revive = revive.astype(int)

newboard = ((~(kill) & initial_state.flatten()) | revive)
newboard = newboard.astype(int)
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print(initial_state.flatten())
print(revive)
print(np.array(newboard).reshape(init_state_shape[0],init_state_shape[1]))

# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(np.array(newboard).reshape(height,width))

    
   
    
    




