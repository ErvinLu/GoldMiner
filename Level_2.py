import heapq #CREATE HEAP
from GoldMiner_v2 import *

#GLOBAL
#self = None
stor_pawn_x = []
stor_pawn_y = []
stor_pawn_dir = []

#PAWN CLASS
class pawn(object):
    def __init__(self, x, y, reachable):
        #REACHABLE = NOT PIT
        #X PAWN = X COORDINATE
        #Y PAWN = Y COORDINATE
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f
#END PAWN CLASS

#A-STAR
class a_star(object):

    # global size
    # global pit_loc
    # global start
    # global end

    def __init__(self):
        self.opened = []
        heapq.heapify(self.opened) #MIN HEAP (LOWEST ON TOP)
        self.closed = set()
        self.cells = []
        self.grid_height = None
        self.grid_width = None

    #INIT GRID
    def init_grid(self, size, pit_loc, start, end):

        self.grid_height = size
        self.grid_width = size

        for x in range(self.grid_width):
            for y in range(self.grid_height):
                if (x, y) in pit_loc:
                    reachable = False
                else:
                    reachable = True
                self.cells.append(pawn(x, y, reachable))

        self.start = self.track_cell(*start)
        self.end = self.track_cell(*end)
    #END INIT GRID

    #HEURISTIC
    def compute_heuristic(self, cell):
        #RETURN H VALUE
        return 10 * (abs(cell.x - self.end.x) + abs(cell.y - self.end.y))
    #END HEURISTIC

    #TRACK CELL
    def track_cell(self, x, y):
        #RETURN X AND Y COORDINATE
        return self.cells[x * self.grid_height + y]
    #END TRACK CELL

    #ADJACENT CELLS
    def adjacent_cells(self, cell):

        # global stor_pawn_x
        # global stor_pawn_y
        global stor_pawn_dir

        cells = []
        if cell.x < self.grid_width - 1:
            cells.append(self.track_cell(cell.x + 1, cell.y))
            direction_level_2 = 2
            # stor_pawn_x.append(cell.x)
            # stor_pawn_y.append(cell.y)
            stor_pawn_dir.append(direction_level_2)
        if cell.y > 0:
            cells.append(self.track_cell(cell.x, cell.y - 1))
            direction_level_2 = 4
            # stor_pawn_x.append(cell.x)
            # stor_pawn_y.append(cell.y)
            stor_pawn_dir.append(direction_level_2)
        if cell.x > 0:
            cells.append(self.track_cell(cell.x - 1, cell.y))
            direction_level_2 = 1
            # stor_pawn_x.append(cell.x)
            # stor_pawn_y.append(cell.y)
            stor_pawn_dir.append(direction_level_2)
        if cell.y < self.grid_height - 1:
            cells.append(self.track_cell(cell.x, cell.y + 1))
            direction_level_2 = 3
            # stor_pawn_x.append(cell.x)
            # stor_pawn_y.append(cell.y)
            stor_pawn_dir.append(direction_level_2)
        return cells
    #END ADJACENT CELLS

    #DISPLAY PATH
    def display_path(self):

        global stor_pawn_x
        global stor_pawn_y

        stor_pawn_x.append(self.end.x)
        stor_pawn_y.append(self.end.y)

        cell = self.end
        path = [(cell.x, cell.y)]
        while cell.parent is not self.start:
            cell = cell.parent
            path.append((cell.x, cell.y))

            stor_pawn_x.append(cell.x)
            stor_pawn_y.append(cell.y)

        path.append((self.start.x, self.start.y))
        path.reverse()

        stor_pawn_x.append(self.start.x)
        stor_pawn_y.append(self.start.y)

        return path
    #END DISPLAY PATH

    #CALCULATE F, G, H
    def update_cell(self, adj, cell):
        adj.g = cell.g + 10
        adj.h = self.compute_heuristic(adj)
        adj.parent = cell
        adj.f = adj.g + adj.h
    #END UPDATE CELL

    #LEVEL 2
    def level_2(self):
        #OPEN HEAP
        heapq.heappush(self.opened, (self.start.f, self.start))
        while len(self.opened):
            #POP CELL FROM HEAP QUEUE
            f, cell = heapq.heappop(self.opened)
            #ADD CELL TO CLOSED LIST (FINAL LIST) [PREVENT DOUBLE PROCESING]
            self.closed.add(cell)
            #IF EXIT CELL CRITERIA ENCOUNTERED, DISPLAY PATH
            if cell is self.end:
                return self.display_path()
                #break

            #GET ADJACENT CELLS FOR CELL
            adj_cells = self.adjacent_cells(cell)
            for adj_cell in adj_cells:
                if adj_cell.reachable and adj_cell not in self.closed:
                    if (adj_cell.f, adj_cell) in self.opened:
                        #IF ADJACENT CELL IS IN OPEN LIST
                        #CHECK IF CURRENT PATH IS BETTER THAN PREVIOUS PATH
                        #FOR THE ADJACENT CELL
                        if adj_cell.g > cell.g + 10:
                            self.update_cell(adj_cell, cell)
                    else:
                        self.update_cell(adj_cell, cell)
                        #ADD ADJACENT CELL TO OPEN LIST
                        heapq.heappush(self.opened, (adj_cell.f, adj_cell))
    #END LEVEL 2
#END A-STAR