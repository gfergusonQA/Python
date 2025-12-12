# NAME: Gina Ferguson
# DATE: 11/17/2025
#   HW: #5 Maze
# Language: Python

import numpy as np
from collections import deque

# Menu-driven by user to determine size of maze rows and columns
def build_maze(n):
    """
    Return the 'no walls' adjacency list for an n x n grid
    nodes labeled as 1..n^2 in row-major order
    """
    maze_no_walls = {}
    for k in range(n * n):
        row = k // n  # division + floor to nearest integer
        col = k % n
        node = k + 1
        neighbors = []

        # up
        if row > 0:
            neighbors.append((row - 1) * n + col + 1)
        # down 
        if row < n - 1:
            neighbors.append((row + 1) * n + col + 1)
        # left
        if col > 0:
            neighbors.append(row * n + (col - 1) + 1)
        # right
        if col < n - 1:
            neighbors.append(row * n + (col + 1) + 1)

        maze_no_walls[node] = neighbors
    return maze_no_walls

# Non-user-driven creation of a 3x3 maze 
# An undirected graph as a dictionary
# 3x3 Maze, all possible neighbors, no walls
# maze_no_walls = {
#    1: [2,4],
#    2: [1,3,5],
#    3: [2,6],
#    4: [1,5,7],
#    5: [2,4,6,8],
#    6: [3,5,9],
#    7: [4,8],
#    8: [5,7,9],
#    9: [6,8]
#}

# ------------------------------
# generating random single maze as an adjacency list on cells 1-9
# ------------------------------
def generate_random_maze(n):
    """
    Return a random maze as an adjacency list (dictionary) on cells 1-9.
    Each possible edge s kept with probability 0.5 aka 50%
    """
    maze_no_walls = build_maze(n)
    adj = {i: [] for i in range(1, n * n + 1)}
    
    for i in range(1, n * n + 1):
        for j in maze_no_walls[i]:
            if i < j:                       # handle each edge only once
                if np.random.rand() > 0.5:  # keep edge with 50% probability
                    adj[i].append(j)
                    adj[j].append(i)
    return adj

# ---------------------------
# Breadth-first search that checks reachability (aka walls or not)
# ---------------------------
def is_solvable(adj, start, goal):
    return find_path(adj, start, goal) is not None
# ---------------------------------------------------------
# Breadth-First Search usage here to make a list of cell #s
# ---------------------------------------------------------

def find_path (adj, start, goal):
    """Return one path from start to goal"""
    visited = set([start])
    parent = {start: None}
    queue = deque([start])

    while queue: 
        current = queue.popleft()
        if current == goal:
            # reconstruct path from goal
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path
        for neighbor in adj[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
    # no path
    return None

# ---------------------------
# Clearly defining start and end cells fo the maze
# ---------------------------
def start_and_goal(n):
    start = n               # top-right cell
    goal = (n - 1) * n + 1  # bottom-left cell
    return start, goal

# ---------------------------
# Create 1000 random mazes to test
# ---------------------------
def one_thousand_mazes(num_mazes=1000, n=3):
    start, goal = start_and_goal(n)
    solvable_count = 0

    for _ in range(num_mazes):
        maze = generate_random_maze(n)
        if is_solvable(maze, start=start, goal=goal):
            solvable_count += 1

    print(f"{solvable_count} out of {num_mazes} mazes were solvable.")
    print(f"That's {solvable_count/num_mazes:.1%} solvable.")

# --------------------------
# Draw maze for user to see what was solved or not solved visually
# --------------------------
def draw_maze(adj, n):    
    def connected(a, b):
        return b in adj[a] or a in adj[b]
    print("\nASCII Maze:")
    # top border
    print("+" + ("---+" * n))
    
    for row in range(n):
        # row of cells w vertical openings
        line = "|"
        for col in range(n):
            cell = row * n + col + 1
            line += f" {cell:2} " 
            if col < n - 1:
                right = cell + 1
                line += " " if connected(cell, right) else "|"
            else:
                line += "|"
        print(line)

        # adding horizontal walls between the rows
        if row < n - 1:
            wall_line = "+"
            for col in range(n):
                cell = row * n + col + 1
                below = cell + n
                if connected(cell, below):
                    wall_line += "   +"     #opening
                else:
                    wall_line += "---+"     #wall
            print(wall_line)
    # bottom border
    print("+" + ("---+" * n))

# --------------------------
# MAIN PROGRAM: 
#   User-driven menu I like to do just in my c++ programs
# --------------------------
def menu():
    quit_commands = {"3", "q", "Q", "quit", "QUIT", "Quit"}

    choice = None 
    # better for tracking bugs than a "While True" loop
    while choice not in quit_commands:    # loop UNTIL user quits
      print("\nWelcome to Gina's Maze Program!")
      print("1) Generate one random maze and check if it is solvable")
      print("2) Run 1000-maze experiment")
      print("3) Quit")

      choice = input("Enter choice (1 - 3): ").strip()
      # .strip() removes extra spaces & more and cleans up user input

      if choice in quit_commands:
        print("Thanks and goodbye!")
        break

      # ask user for grid size ( rrows = cols = n )
      # n = int(input("Enter maze size n (i.e. 3 for 3x3, 5 for 5x5): "))
      # Error Handling for no input from user if they tap only "Enter"
      user_input = input("Enter maze size n (i.e. 3 for 3x3, 5 for 5x5): ").strip()

      if not user_input.isdigit():
          print("Invalid input or nothing entered. Defaulting to n = 3.")
          n = 3
      else:
          n = int(user_input)

      if choice == "1":
        start, goal = start_and_goal(n)
        maze = generate_random_maze(n)
        print(f"\nChecking single maze {n}x{n} from {start} to {goal}...")

        # show the maze
        draw_maze(maze, n)

        path = find_path(maze, start, goal)
        if path is None:
            print("Solvable? False... (no path found)")
        else:
            print("Solvable? True")
            print("One path from start to goal:", path)
      elif choice == "2":
        one_thousand_mazes(1000, n=n)
      else:
        print("Invalid! Please try again and stick to the menu options.")


# --------------------------
# RUN PROGRAM
# --------------------------
if __name__ == "__main__":
    menu()
