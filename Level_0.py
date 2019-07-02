import random
from GoldMiner_v2 import *

stor_pawn_x = []
stor_pawn_y = []
stor_pawn_dir = []

def level_0(pawn_x, pawn_y, maze):
    # pawn_x = 0
    # pawn_y = 0
    global stor_pawn_x
    global stor_pawn_y
    global stor_pawn_dir

    rand_value = random.randint(1,2)

    if maze[pawn_x][pawn_y] == 'G':
        print("Found Gold at", (pawn_x, pawn_y))
        return True #EXIT WHEN GOLD IS FOUND
    elif maze[pawn_x][pawn_y] == 'P':
        print("Found Pit at", (pawn_x, pawn_y))
        return True #EXIT WHEN PIT IS STEPPED ON #SET TO FALSE TO AVOID PITS
    elif maze[pawn_x][pawn_y] == 'B':
        print("Found Beacon at", (pawn_x, pawn_y))
        return False
    elif maze[pawn_x][pawn_y] == 'V':
        print("Node Visited at", (pawn_x, pawn_y))
        return False

    print("Currently on", (pawn_x, pawn_y))

    #MARK VISITED
    #maze[pawn_x][pawn_y] = 'V'

    # display_maze(len(maze), maze)
    # print("*********************************")

    #rand_value = 1

    #EXPLORE NEIGHBORS CLOCKWISE STARTING FROM THE ONE ON THE RIGHT
    if rand_value == 1: #TOP-DOWN LEFT-RIGHT
        if (pawn_x < len(maze) - 1 and level_0(pawn_x + 1, pawn_y, maze)):
            direction_level_0 = 2
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE",(pawn_x, pawn_y))
            # direction_level_0 = 2
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '↓'
            return True
        if (pawn_y > 0 and level_0(pawn_x, pawn_y - 1, maze)):
            direction_level_0 = 4
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 4
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '←'
            return True
        if (pawn_x > 0 and level_0(pawn_x - 1, pawn_y, maze)):
            direction_level_0 = 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 1
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '↑'
            return True
        if (pawn_y < len(maze) - 1 and level_0(pawn_x, pawn_y + 1, maze)):
            direction_level_0 = 3
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 3
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '→'
            return True
    elif rand_value == 2: #RIGHT-LEFT TOP-DOWN
        if (pawn_y < len(maze) - 1 and level_0(pawn_x, pawn_y + 1, maze)):
            direction_level_0 = 3
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 3
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '→'
            return True
        if (pawn_x > 0 and level_0(pawn_x - 1, pawn_y, maze)):
            direction_level_0 = 1
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 1
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '↑'
            return True
        if (pawn_y > 0 and level_0(pawn_x, pawn_y - 1, maze)):
            direction_level_0 = 4
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 4
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '←'
            return True
        if (pawn_x < len(maze) - 1 and level_0(pawn_x + 1, pawn_y, maze)):
            direction_level_0 = 2
            stor_pawn_x.append(pawn_x)
            stor_pawn_y.append(pawn_y)
            stor_pawn_dir.append(direction_level_0)
            # print("MOVEEEE", (pawn_x, pawn_y))
            # direction_level_0 = 2
            # print("Direction:", (direction_level_0))
            #maze[pawn_x][pawn_y] = '↓'
            return True

    return False