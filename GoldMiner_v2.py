import random

from Level_0 import *
from Level_2 import *

#GLOBAL
size = 0    #MATRIX SIZE
move_x = 0  #PATH X
move_y = 0  #PATH Y
curr_x = 0  #CURRENT X POSITION AGENT
curr_y = 0  #CURRENT Y POSITION AGENT
gold_x = 0
gold_y = 0
start = (0,0)
end = (0,0)
pit_count = 0
pit_loc = []
maze = None #REFERENCE MAZE
init_maze_res = None    #INITIALIZE MAZE RESULT
direction = 0   #AGENT DIRECTION

#ROTATE
def rotate(direction):
    #dir_value = '→' #DEFAULT WILL BE FACE RIGHT (SHOULD BE REPLACED BY PREV VALUE IF UNCHANGED)
    dir_value = '↓'  # DEFAULT WILL BE FACE RIGHT (SHOULD BE REPLACED BY PREV VALUE IF UNCHANGED)

    if direction == 1:
        dir_value = '↑' #FACE UP
    elif direction == 2:
        dir_value = '↓' #FACE DOWN
    elif direction == 3:
        dir_value = '→' #FACE RIGHT
    elif direction == 4:
        dir_value = '←' #FACE LEFT
    return dir_value
#END ROTATE

#SCAN
def scan(size, direction):
    global init_maze_res
#END SCAN

#MOVE
def move(size, direction, init_maze_res):
    global maze
    global move_x, move_y
    global curr_x, curr_y

    prev_x = curr_x
    prev_y = curr_y

    prev_value = maze[prev_x][prev_y]
    print("prev value from ref: " + prev_value)

    if direction == 1:      #FACE UP
        curr_x = prev_x
        curr_y = prev_y + 1
    elif direction == 2:    #FACE DOWN
        curr_x = prev_x
        curr_y = prev_y - 1
    elif direction == 3:    #FACE RIGHT
        curr_x = prev_x + 1
        curr_y = prev_y
    elif direction == 4:    #FACE LEFT
        curr_x = prev_x - 1
        curr_y = prev_y

    orig_prev_value = maze[curr_x][curr_y]
    print("moving to this: " + str(orig_prev_value))
    init_maze_res[curr_x][curr_y] = prev_value

    if maze[prev_x][prev_y] is not 'G' or maze[prev_x][prev_y] is not 'P' or maze[prev_x][prev_y] is not 'B':
        init_maze_res[prev_x][prev_y] = 0
    else:
        init_maze_res[prev_x][prev_y] = orig_prev_value
#END MOVE

#INITIALIZE MAZE
def init_maze(size, maze):

    global init_maze_res

    #maze is the REFERENCE MAZE VALUE

    #maze[0][0] = '0'  # STARTING POINT AT 0,0 FACING RIGHT
    #maze[0][0] = '→' #STARTING POINT AT 0,0 FACING RIGHT
    maze[0][0] = '↓'  # STARTING POINT AT 0,0 FACING RIGHT

    curr_x = 0
    curr_y = 0

    global gold_x
    global gold_y
    global end

    global pit_loc  #FORGOT IF NEEDED 7/2/2019

    #GOLD POSITION
    gold_x = int(input("Gold X Location: "))
    gold_y = int(input("Gold Y Location: "))
    end = (gold_x - 1, gold_y - 1)
    maze[gold_x - 1][gold_y - 1] = 'G' #GOLD PLACED AT LOCATION (-1 FOR COMPENSATION)
    #END GOLD POSITION

    #BEACON POSITION
    beacon_count = int(input("Enter number of beacons: "))
    for i in range(beacon_count):
        beacon_x = int(input("Beacon[" + str(i + 1) + "] X Location: "))
        beacon_y = int(input("Beacon[" + str(i + 1) + "] Y Location: "))

        maze[beacon_x - 1][beacon_y - 1] = 'B'
    #END BEACON POSITION

    # PIT POSITION
    pit_count = int(input("Enter number of pits: "))
    for i in range(pit_count):
        pit_x = int(input("Pit[" + str(i + 1) + "] X Location: "))
        pit_y = int(input("Pit[" + str(i + 1) + "] Y Location: "))

        maze[pit_x - 1][pit_y - 1] = 'P'

        where_the_pit = (pit_x - 1, pit_y - 1)
        pit_loc.append(where_the_pit)
    # END PIT POSITION
    init_maze_res = maze
#END INITIALIZE MAZE

#DISPLAY MAZE
def display_maze(size, maze):
    for i in maze:
        # print(maze[i],[i]) #CHECK CONTENTS
        print(*i, sep="\t")
# END DISPLAY MAZE

#LEVEL 0
# def level_0(pawn_x, pawn_y, maze):
#     # pawn_x = 0
#     # pawn_y = 0
#     rand_value = random.randint(1,2)
#
#     if maze[pawn_x][pawn_y] == 'G':
#         print("Found Gold at", (pawn_x + 1, pawn_y + 1))
#         return True #EXIT WHEN GOLD IS FOUND
#     elif maze[pawn_x][pawn_y] == 'P':
#         print("Found Pit at", (pawn_x + 1, pawn_y + 1))
#         return True #EXIT WHEN PIT IS STEPPED ON
#     elif maze[pawn_x][pawn_y] == 'B':
#         print("Found Beacon at", (pawn_x + 1, pawn_y + 1))
#         #return False
#     elif maze[pawn_x][pawn_y] == 'V':
#         print("Node Visited at", (pawn_x + 1, pawn_y + 1))
#         return False
#
#     print("Currently on", (pawn_x + 1, pawn_y + 1))
#
#     #MARK VISITED
#     maze[pawn_x][pawn_y] = 'V'
#
#     display_maze(len(maze), maze)
#     print("*********************************")
#
#     #rand_value = 2
#
#     #EXPLORE NEIGHBORS CLOCKWISE STARTING FROM THE ONE ON THE RIGHT
#     if rand_value == 1: #TOP-DOWN LEFT-RIGHT
#         if ((pawn_x < len(maze) - 1 and level_0(pawn_x + 1, pawn_y, maze))
#             or (pawn_y > 0 and level_0(pawn_x, pawn_y - 1, maze))
#             or (pawn_x > 0 and level_0(pawn_x - 1, pawn_y, maze))
#             or (pawn_y < len(maze) - 1 and level_0(pawn_x, pawn_y + 1, maze))):
#             return True
#     elif rand_value == 2: #LEFT-RIGHT TOP-DOWN
#         if ((pawn_y < len(maze) - 1 and level_0(pawn_x, pawn_y + 1, maze))
#             or (pawn_x > 0 and level_0(pawn_x - 1, pawn_y, maze))
#             or (pawn_y > 0 and level_0(pawn_x, pawn_y - 1, maze))
#             or (pawn_x < len(maze) - 1 and level_0(pawn_x + 1, pawn_y, maze))):
#             return True
#
#     return False
#END LEVEL 0


def main():
    global maze
    global start
    global end
    global size
    size = int(input("Enter playing field size: "))
    maze = [[0 for x in range(size)] for y in range(size)] #INITIALIZE MAZE

    init_maze(size, maze)
    print("INITIAL MAZE")
    display_maze(size, init_maze_res)

    # #LEVEL 0
    # global stor_pawn_x
    # global stor_pawn_y
    # global stor_pawn_dir
    # print("*********************************")
    # level_0(0,0,init_maze_res)
    #
    # stor_pawn_x.reverse()
    # stor_pawn_y.reverse()
    # stor_pawn_dir.reverse()
    #
    # for i in range(len(stor_pawn_x)):
    #     if stor_pawn_dir[i] == 1:
    #         init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
    #     if stor_pawn_dir[i] == 2:
    #         init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
    #     if stor_pawn_dir[i] == 3:
    #         init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
    #     if stor_pawn_dir[i] == 4:
    #         init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'
    #
    #     print("ITERATION", (i))
    #     display_maze(size, init_maze_res)
    #     print("*********************************")
    # #END LEVEL 0

    #LEVEL 2
    print("*********************************")
    level_2 = a_star()
    level_2.init_grid(size, pit_loc, start, end)
    path = level_2.level_2()
    print(path)

    stor_pawn_x.append(0)   #BUFFER FOR INITIAL START POSITION
    stor_pawn_y.append(0)   #BUFFER FOR INITIAL START POSITION

    stor_pawn_x.reverse()
    stor_pawn_y.reverse()
    stor_pawn_dir.reverse()

    for i in range(len(stor_pawn_x) - 1):
        # if stor_pawn_dir[i] == 1:
        #     init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
        # if stor_pawn_dir[i] == 2:
        #     init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
        # if stor_pawn_dir[i] == 3:
        #     init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'
        # if stor_pawn_dir[i] == 4:
        #     init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'
        if (stor_pawn_x[i+1] == stor_pawn_x[i] + 1) and (stor_pawn_y[i+1] == stor_pawn_y[i]):
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↓'
        if (stor_pawn_x[i+1] == stor_pawn_x[i]) and (stor_pawn_y[i+1] == stor_pawn_y[i] - 1):
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '↑'
        if (stor_pawn_x[i+1] == stor_pawn_x[i] - 1) and (stor_pawn_y[i+1] == stor_pawn_y[i]):
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '←'
        if (stor_pawn_x[i+1] == stor_pawn_x[i]) and (stor_pawn_y[i+1] == stor_pawn_y[i] + 1):
            init_maze_res[stor_pawn_x[i]][stor_pawn_y[i]] = '→'

        print("ITERATION", (i))
        display_maze(size, init_maze_res)
        print("*********************************")
    #END LEVEL 2

    # while ((curr_x < size) and (curr_y < size)) or (init_maze_res[curr_x][curr_y] is not 'P' or init_maze_res[curr_x][curr_y] is not 'G'):
    #     move(size, 1, init_maze_res)
    #     print("MOVE RIGHT")
    #     display_maze(size, init_maze_res)

    #print(maze)

    #print(pit_loc[0])

    # for i in range(5):
    #     direction = rotate(random.randint(1,5))
    #     print(direction)

if __name__ == '__main__':
    main()