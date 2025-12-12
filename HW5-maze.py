# In-class Maze Practice
# Python example: 
# all possible neighbors for cells in a 3x3 maze (dictionary in python)

import numpy as np
maze_no_walls = {
    1: [2,4],
    2: [1,3,5],
    3: [2,6],
    4: [1,5,7],
    5: [2,4,6,8],
    6: [3,5,9],
    7: [4,8],
    8: [5,7,9],
    9: [6,8]
}

adj_list_random_maze = maze_no_walls.copy()
for i in range(1,10):
    adj_list_random_maze[i] = []

    # Loop over all possible edges in the graph, toss a 50-50 coin, and 
    # decide whether to keep the edge or discard it. Careful to maintain 
    # undirected graph.
for i in range(1,10):                  # loop over all cells, 1-9=(1,10)
    for j in maze_no_walls[i]:         # loop over possible neighbors of that cell
        if np.random.rand() <= 0.5:    # numpy package & rand(), flip a coin
            pass
        else:
            adj_list_random_maze[i].append(j)   # all edges are "bidirectional" to 
                                                # maintain bidirectional-ness
            adj_list_random_maze[i].append(i)                                  

# Print out each cell and its open paths (no walls):
for cell in range(1,10):
    print(f"Cell {cell}: neighbors -> {adj_list_random_maze[cell]}")

# Print out only the walls
print("\nWalls:")
for cell in range(1,10):
        for neighbor in maze_no_walls[cell]:
                if neighbor not in adj_list_random_maze[cell]:
                    print(f"Wall between {cell} and {neighbor}")

# ASCII 3x3 MAZE Drawing based on the cell and neighbor data, and adjacency list
def draw_maze(adj):
    cells = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    def connected(a, b):
        # true if there is a passage between a and b
        return b in adj[a] or a in adj[b]

    # top border
    print("+---+---+---+")
    for r in range(3):
        # row with cell numbers and vertical walls
        line = "|"
        for c in range(3):
            cell = cells[r][c]
            line += f" {cell} "
            if c < 2: #between this cell and one to the right
                right = cells[r][c + 1]
                if connected(cell, right):
                    line += " "     # opening
                else:
                    line += "|"     # wall
            else:
                line += "|"         # right outer border
        print(line)

        # horizontal walls under this row
        line = "+"
        for c in range(3):
            cell = cells[r][c]
            if r < 2:               # between this row and the one below
                below = cells[r+1][c]
                if connected(cell, below):
                    line += "   "   # opening
                else:
                    line += "---"   # wall
            else:
               line += "---"        # bottom outer border
            line += "+"
        print(line)

draw_maze(adj_list_random_maze)
