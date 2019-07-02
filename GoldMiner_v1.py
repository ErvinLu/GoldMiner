import random

#GLOBAL
gold_x = 0
gold_y = 0
start = (0,0)
end = (0,0)
pit_count = 0
pit_loc = []
init_maze_res = None

#PAWN CLASS
class pawn():

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0 #FOR A-STAR
        self.h = 0 #FOR A-STAR
        self.f = 0 #FOR A-STAR

    def __eq__(self, other):
        return self.position == other.position
#END PAWN CLASS

#LEVEL 0
def level_0(size, maze, start, end):
    #direction = random.randint(1,5)
    start_node = pawn(None, start)
    start_node.g = start_node.h = start_node.f = 0 #FOR ASTAR
    #end = (gold_x - 1, gold_y - 1)
    end_node = pawn(None, end)
    end_node.g = end_node.h = end_node.f = 0 #FOR ASTAR

    #INITIALIZE path
    open_path_list = []
    closed_path_list = []

    #ADD THE START NODE
    open_path_list.append(start_node)

    #LOOP UNTIL END OR PIT
    while len(open_path_list) > 0:
        #GET CURRENT NODE
        current_node = open_path_list[0]
        current_index = 0
        for index, item in enumerate(open_path_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        #POP CURRENT FROM OPEN LIST, ADD TO CLOSED LIST
        open_path_list.pop(current_index)
        closed_path_list.append(current_node)

        # PIT IS FOUND
        # for pit_found in pit_loc:
        #     if current_node == pawn(None, pit_loc[pit_found]):
        #         path = []  # RETURN THE TRAVERSED PATH
        #         current = current_node
        #         while current is not None:
        #             path.append(current.position)
        #             current = current.parent
        #         return path[::-1]  # RETURN THE TRAVERSED PATH

        #GOAL IS FOUND
        if current_node == end_node:
            path = [] #RETURN THE TRAVERSED PATH
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] #RETURN THE TRAVERSED PATH


        #POSSIBLE MOVES/CHILDREN
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: #ADJACENT SQUARES
            #GET NODE POSITION
            #direction = random.randint(1, 5)
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            #MOVE IS WITHIN RANGE
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            #SQUARE IS STILL WALKABLE
            if maze[node_position[0]][node_position[1]] != 0 or maze[node_position[0]][node_position[1]] == 'G':
                continue

            #CREATE NEW NODE
            new_node = pawn(current_node, node_position)

            #APPEND
            children.append(new_node)

            #LOOP THROUGH CHILDREN
        for child in children:

            #CHILD IN CLOSED LIST
            for closed_child in closed_path_list:
                if child == closed_child:
                    continue

            #CHILD IS IN OPEN LIST
            for open_node in open_path_list:
                if child == open_node and current_node.g + 1 > open_node.g:
                    continue

            #ADD CHILD TO OPEN LIST
            open_path_list.append(child)

#END LEVEL 0

#ROTATE
def rotate(direction):
    dir_value = '→' #DEFAULT WILL BE FACE RIGHT (SHOULD BE REPLACED BY PREV VALUE IF UNCHANGED)

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

#INITIALIZE MAZE
def init_maze(size, maze):

    global init_maze_res

    #maze[0][0] = '0'  # STARTING POINT AT 0,0 FACING RIGHT
    maze[0][0] = '→' #STARTING POINT AT 0,0 FACING RIGHT

    global gold_x
    global gold_y
    global end

    #GOLD POSITION
    gold_x = int(input("Gold X Location: "))
    gold_y = int(input("Gold Y Location: "))
    end = (gold_x - 1, gold_y - 1)
    maze[gold_x - 1][gold_y - 1] = 0 #GOLD PLACED AT LOCATION (-1 FOR COMPENSATION)
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



def main():
    global start
    global end
    size = int(input("Enter playing field size: "))
    maze = [[0 for x in range(size)] for y in range(size)] #INITIALIZE MAZE

    init_maze(size, maze)
    display_maze(size, init_maze_res)

    path = level_0(size, init_maze_res, start, end)
    print(path)

    print(maze)

    #print(pit_loc[0])

    # for i in range(5):
    #     direction = rotate(random.randint(1,5))
    #     print(direction)

if __name__ == '__main__':
    main()