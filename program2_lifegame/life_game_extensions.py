import numpy as np
from time import sleep
f = open('Gun.txt')
text_list = f.readlines()
# print(text_list)

integer_list = []
counter = np.zeros(2).astype(int)#制造一个数是0的一维数组，只有两个元素
counter[0]=1
for element in text_list:
    counter[1]=0
    for ch in element:
        if not(ch == '\n'):
            integer_list.append(int(ch))
            counter[1]+=1
        else:
            counter[0]+=1
        # print(counter)

text_array = np.array(integer_list)
text_array_reshape = text_array.reshape(counter)
print(text_array_reshape)

# =============================================================================
# another way to change the string in the file to integer array
# =============================================================================
# =============================================================================
# f = open('toad.txt')
# text_list = f.readlines()
# print(text_list)
# 
# integer_list = []
# # counter = np.zeros(2).astype(int)
# # print(counter)
# # counter[1]=1
# for element in text_list:
#     # counter[0]=0
#     for ch in element:
#         if not(ch == '\n'):
#             integer_list.append(int(ch))
# 
# text_array = np.array(integer_list)
# text_array_reshape = text_array.reshape(6,6)
# =============================================================================


initial_state = text_array_reshape

def next_board_state(init_state):

    new_state =[]
    a=b=c=d=e=f=g=h=live_total = 0
    init_state_shape = init_state.shape
    for y in range(init_state_shape[0]):
        for x in range(init_state_shape[1]):
            # one cell around by 8 neighbors
            if 0<y<(init_state_shape[0]-1) and 0<x<(init_state_shape[1]-1):
                a = init_state[y-1][x-1]
                b = init_state[y-1][x]
                c = init_state[y-1][x+1]
                d = init_state[y][x-1]
                e = init_state[y][x+1]
                f = init_state[y+1][x-1]
                g = init_state[y+1][x]
                h = init_state[y+1][x+1]
                live_total = a+b+c+d+e+f+g+h
            # upleft corner cell around by 3 neighbors
            elif x==0 and y==0:
                e = init_state[y][x+1]
                g = init_state[y+1][x]
                h = init_state[y+1][x+1]
                live_total = e+g+h
           
            # upright corner cell around by 3 neighbors
            elif y==0 and x==(init_state_shape[1]-1):
                d = init_state[y][x-1]
                f = init_state[y+1][x-1]
                g = init_state[y+1][x]
                live_total = d+f+g
          
            # bottomleft corner cell around by 3 neighbors
            elif y ==(init_state_shape[0]-1) and x == 0:
                b = init_state[y-1][x]
                c = init_state[y-1][x+1]
                e = init_state[y][x+1]
                live_total = b+c+e               
            
            # bottomright corner cell around by 3 neighbors    
            elif y ==(init_state_shape[0]-1) and x ==(init_state_shape[1]-1):
                a = init_state[y-1][x-1]
                b = init_state[y-1][x]
                d = init_state[y][x-1]
                live_total = a+b+d
          
            # up line cells arounded by 5 neighbors
            elif y==0 and 0<x<(init_state_shape[1]-1):
                d = init_state[y][x-1]
                e = init_state[y][x+1]
                f = init_state[y+1][x-1]
                g = init_state[y+1][x]
                h = init_state[y+1][x+1]
                live_total = d+e+f+g+h
            # bottom line cells arounded by 5 neighbors
            elif y==(init_state_shape[0]-1) and  0<x<(init_state_shape[1]-1):
                a = init_state[y-1][x-1]
                b = init_state[y-1][x]
                c = init_state[y-1][x+1]
                d = init_state[y][x-1]
                e = init_state[y][x+1]
                live_total = a+b+c+d+e
             #left line cells arounded by 5 neighbors
            elif x == 0 and 0<y<(init_state_shape[0]-1):
               b = init_state[y-1][x]
               c = init_state[y-1][x+1]
               e = init_state[y][x+1]
               g = init_state[y+1][x]
               h = init_state[y+1][x+1]
               live_total = b+c+e+g+h
              #right line cells arounded by 5 neighbors
            elif x == (init_state_shape[1]-1) and 0<y<(init_state_shape[0]-1):
               a = init_state[y-1][x-1]
               b = init_state[y-1][x]
               d = init_state[y][x-1]
               f = init_state[y+1][x-1]
               g = init_state[y+1][x]
               live_total = a+b+d+f+g
            new_state.append(live_total) 
            

    dimensional_new_state = np.array(new_state)

# if neighbor cell living number is 0,1 and more than 3, state is 0
# whatever the initial state is 0 or 1
    kill = ((dimensional_new_state<=1)|(dimensional_new_state >3))

    revive = (dimensional_new_state==3)
    revive = revive.astype(int)

# not kill :neighbor cell living number is 2 and 3, 1&2,3=1
# 0&2=0, 0&3 =1 -> revive
    newboard = ((~(kill) & init_state.flatten()) | revive)
    newboard = newboard.astype(int)
    newboard_reshape = np.array(newboard).reshape(init_state_shape[0],init_state_shape[1])
    return newboard_reshape,dimensional_new_state.reshape(init_state_shape)


# print(initial_state)
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(next_board_state(initial_state))
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(next_board_state(next_board_state(initial_state)))
# =============================================================================
# change the element in the array using characters whatever i like   
# =============================================================================

def render_fuction(new_array):
    cell_state = []
    cell_sate_value = 0
    shape = new_array.shape
    for k in range (shape[0]):
        for p in range (shape[1]):
            if new_array[k][p] == 0:
                cell_sate_value = " "
            else:
                cell_sate_value = "#"
            cell_state.append(cell_sate_value)
    new_array1_reshape = np.array(cell_state).reshape(shape)    
    return new_array1_reshape

# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(render_fuction(next_board_state(initial_state)))
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# print(render_fuction(next_board_state(next_board_state(initial_state))))
# =============================================================================
# Run Life forever            
# =============================================================================
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


while True:
    aa,ee = next_board_state(initial_state)
    bb = render_fuction(aa)
    sh = bb.shape[1]
    for row in bb[:]:
        print(''.join(row))#change to string from array
    #print(initial_state)
    #print(ee)
    initial_state = aa
    sleep(0.050)
