import numpy as np
from life_game import next_board_state


# TODO: there's a lot of repeated code here. Can
# you move some of into reusable functions to
# make it shorter and neater?

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    init_state1 = np.array(init_state)
    # print(init_state1)
    expected_next_state0 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = np.array(expected_next_state0)
    # print(expected_next_state1)
    
    actual_next_state1 = next_board_state(init_state1)

    if  expected_next_state1.all() == actual_next_state1.all():
        print ("PASSED 1")
    else:
        print ("FAILED 1!")
        print ("Expected:")
        print (expected_next_state1)
        print ("Actual:")
        print (actual_next_state1)
        
        
        
# TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state_02 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    init_state2 = np.array(init_state_02)
    
    expected_next_state002 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]

    actual_next_state2 = next_board_state(init_state2)
    expected_next_state2 = np.array(expected_next_state002)
    if expected_next_state2.all() == actual_next_state2.all():
        print ("PASSED 2")
    else:
        print ("FAILED 2!")
        print ("Expected:")
        print (expected_next_state2)
        print ("Actual:")
        print (actual_next_state2)

# =============================================================================
#  How could you check that live cells die
#  when they have more than 3 live neighbors? 
#  How could you make sure that everything works
#  as expected for cells on the edges of the board 
#  and in the corners?
# =============================================================================


# TEST 3: dead cells with more than 3 neighbors
    # should come alive.
    init_state_03 = [
        [0,0,1],
        [0,1,1],
        [1,1,0]
    ]
    init_state3 = np.array(init_state_03)
    
    expected_next_state003 = [
        [0,1,1],
        [1,0,1],
        [1,1,1]
    ]

    actual_next_state3 = next_board_state(init_state3)
    expected_next_state3 = np.array(expected_next_state003)
    if expected_next_state3.all() == actual_next_state3.all():
        print ("PASSED 3")
    else:
        print ("FAILED 3!")
        print ("Expected:")
        print (expected_next_state3)
        print ("Actual:")
        print (actual_next_state3)

# TEST 4: dead cells in the edge corners
    # should come alive.
    init_state_04 = [
        [0,1,0],
        [1,1,1],
        [1,0,0]
    ]
    init_state4 = np.array(init_state_04)
    
    expected_next_state004 = [
        [1,1,1],
        [1,0,1],
        [1,0,0]
    ]

    actual_next_state4 = next_board_state(init_state4)
    expected_next_state4 = np.array(expected_next_state004)
    if expected_next_state4.all() == actual_next_state4.all():
        print ("PASSED 4")
    else:
        print ("FAILED 4!")
        print ("Expected:")
        print (expected_next_state4)
        print ("Actual:")
        print (actual_next_state4)

# TEST 4: lager array
    # should come alive.
    init_state_05 = [
        [0,1,0],
        [1,1,1],
        [1,0,0],
        [1,1,1]
    ]
    init_state5 = np.array(init_state_05)
    
    expected_next_state005 = [
        [1,1,1],
        [1,0,1],
        [0,0,0],
        [1,1,0]
    ]

    actual_next_state5 = next_board_state(init_state5)
    expected_next_state5 = np.array(expected_next_state005)
    if expected_next_state5.all() == actual_next_state5.all():
        print ("PASSED 5")
    else:
        print ("FAILED 5!")
        print ("Expected:")
        print (expected_next_state5)
        print ("Actual:")
        print (actual_next_state5)