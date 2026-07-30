from collections import deque
from queue import PriorityQueue
import math

# ===========================
# Experiment 1 : Maze Escape
# ===========================
def maze_escape():

    maze = [
        ['S', '.', '.', '#', '.'],
        ['#', '#', '.', '#', '.'],
        ['.', '.', '.', '.', '.'],
        ['.', '#', '#', '#', '.'],
        ['.', '.', '.', 'G', '.']
    ]

    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'S':
                start = (i, j)
            if maze[i][j] == 'G':
                goal = (i, j)

    queue = deque()
    queue.append((start, 0))

    visited = set()
    visited.add(start)

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while queue:

        (x, y), steps = queue.popleft()

        if (x, y) == goal:
            print("\nGoal Reached")
            print("Minimum Steps =", steps)
            return

        for dx, dy in directions:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < rows and 0 <= ny < cols:

                if maze[nx][ny] != '#' and (nx, ny) not in visited:

                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))


# ===========================
# Experiment 2 : 12 Queens
# ===========================
def n_queens():

    N = 12
    board = [[0] * N for _ in range(N)]

    def is_safe(row, col):

        for i in range(col):
            if board[row][i]:
                return False

        i = row
        j = col

        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1

        i = row
        j = col

        while i < N and j >= 0:
            if board[i][j]:
                return False
            i += 1
            j -= 1

        return True

    def solve(col):

        if col >= N:
            return True

        for row in range(N):

            if is_safe(row, col):

                board[row][col] = 1

                if solve(col + 1):
                    return True

                board[row][col] = 0

        return False

    if solve(0):

        print("\n12 Queens Solution\n")

        for row in board:
            print(row)

    else:
        print("No Solution")


# ===========================
# Experiment 3 : Water Jug
# ===========================
def water_jug():

    jug1 = 11
    jug2 = 9
    target = 8

    queue = deque()
    queue.append(((0, 0), []))

    visited = set()

    while queue:

        (a, b), path = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))

        path = path + [(a, b)]

        if a == target or b == target:

            print("\nSolution Found\n")

            for state in path:
                print(state)

            print("\nMinimum Moves =", len(path) - 1)
            return

        next_states = [

            (jug1, b),
            (a, jug2),
            (0, b),
            (a, 0),

            (max(0, a - (jug2 - b)), min(jug2, a + b)),
            (min(jug1, a + b), max(0, b - (jug1 - a)))

        ]

        for state in next_states:

            if state not in visited:
                queue.append((state, path))


# ===========================
# Experiment 4 : Connect Four
# (Mini Minimax Demo)
# ===========================
def connect_four():

    board = [

        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']

    ]

    def print_board():

        for row in board:
            print(row)

    def check(player):

        for i in range(3):

            if all(board[i][j] == player for j in range(3)):
                return True

            if all(board[j][i] == player for j in range(3)):
                return True

        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

        return False

    def minimax(ai):

        if check('O'):
            return 1

        if check('X'):
            return -1

        empty = False

        for row in board:
            if '_' in row:
                empty = True

        if not empty:
            return 0

        if ai:

            best = -math.inf

            for i in range(3):
                for j in range(3):

                    if board[i][j] == '_':

                        board[i][j] = 'O'

                        best = max(best, minimax(False))

                        board[i][j] = '_'

            return best

        else:

            best = math.inf

            for i in range(3):
                for j in range(3):

                    if board[i][j] == '_':

                        board[i][j] = 'X'

                        best = min(best, minimax(True))

                        board[i][j] = '_'

            return best

    print("\nConnect Four (Mini Minimax Demonstration)\n")
    print_board()

    print("\nBoard Evaluation =", minimax(True))


# ===========================
# Experiment 5 : 8 Puzzle
# ===========================
def eight_puzzle():

    goal = [1,2,3,4,5,6,7,8,0]

    start = [1,2,3,
             4,0,6,
             7,5,8]

    def heuristic(state):

        count = 0

        for i in range(9):

            if state[i] != goal[i]:
                count += 1

        return count

    pq = PriorityQueue()

    pq.put((heuristic(start),0,start))

    visited = set()

    while not pq.empty():

        f,g,state = pq.get()

        if tuple(state) in visited:
            continue

        visited.add(tuple(state))

        if state == goal:

            print("\nPuzzle Solved")
            print("Minimum Moves =", g)
            return

        zero = state.index(0)

        moves = []

        if zero > 2:
            moves.append(zero - 3)

        if zero < 6:
            moves.append(zero + 3)

        if zero % 3 != 0:
            moves.append(zero - 1)

        if zero % 3 != 2:
            moves.append(zero + 1)

        for move in moves:

            new_state = state[:]

            new_state[zero], new_state[move] = new_state[move], new_state[zero]

            if tuple(new_state) not in visited:

                h = heuristic(new_state)

                pq.put((g + 1 + h, g + 1, new_state))


# ===========================
# Main Menu
# ===========================

while True:

    print("\n========== AI LAB EXPERIMENTS ==========")
    print("1. AI Maze Escape (BFS)")
    print("2. 12-Queens Challenge (Backtracking)")
    print("3. Water Jug Puzzle (BFS)")
    print("4. Connect Four AI (Minimax)")
    print("5. 8-Puzzle (A*)")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        maze_escape()

    elif choice == 2:
        n_queens()

    elif choice == 3:
        water_jug()

    elif choice == 4:
        connect_four()

    elif choice == 5:
        eight_puzzle()

    elif choice == 6:
        print("\nThank You")
        break

    else:
        print("\nInvalid Choice")