moves = ""
map_grid = []

with open("15_input_test.txt") as f:
    reading_map = True
    for line in f:
        line = line.strip()
        # Check if it's part of the map
        if reading_map and line.startswith('#'):
            map_grid.append(list(line))
        elif not line.startswith('#') and line:
            reading_map = False
            moves += line

def locate_player(map_grid):
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] == "@":
                return row, col

def get_dir(symbol):
    if symbol == "<":
        return (0, -1) # row, col
    if symbol == "^":
        return (-1, 0)
    if symbol == ">":
        return (0, 1)
    if symbol == "v":
        return (1, 0)

def push_box(row, col, direction, map_grid):
    new_row, new_col = row + direction[0], col + direction[1]
    if map_grid[new_row][new_col] == ".":
        map_grid[new_row][new_col] = "O"
        map_grid[row][col] = "."
        return new_row, new_col, map_grid
    elif map_grid[new_row][new_col] == "#": # hit a wall, don't move box
        return row, col, map_grid
    elif map_grid[new_row][new_col] == "O":
        next_row, next_col, map_grid = push_box(new_row, new_col, direction, map_grid)
        if (next_row, next_col) != (new_row, new_col):
            map_grid[new_row][new_col] = "O" # Ensure the box is kept when pushing forward
        return next_row, next_col, map_grid

def move_robot_and_push(map_grid, row, col, direction):
    new_row, new_col = row + direction[0], col + direction[1]
    if map_grid[new_row][new_col] == ".":
        map_grid[new_row][new_col] = "@"
        map_grid[row][col] = "."
        return new_row, new_col, map_grid # new location of robot
    elif map_grid[new_row][new_col] == "#": # hit a wall, return same location
        return row, col, map_grid
    elif map_grid[new_row][new_col] == "O":
        box_row, box_col, map_grid = push_box(new_row, new_col, direction, map_grid)
        if (box_row, box_col) == (new_row, new_col):
            return row, col, map_grid # couldn't move the box
        map_grid[new_row][new_col] = "@"
        map_grid[row][col] = "."
        return new_row, new_col, map_grid

def print_map(map_grid):
    for row in map_grid:
        print("".join(row))

def calculate_gps(map_grid):
    gps = 0
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] == "O":
                gps += 100 * row + col
    return gps

start_row, start_col = locate_player(map_grid)
print("start grid\n")
print_map(map_grid)
print("")
move_nr = 0
for move in moves:
    direction = get_dir(move)
    start_row, start_col, map_grid = move_robot_and_push(map_grid, start_row, start_col, direction)
    print("Move nr: ", move_nr, "move symbol: ", move)
    print("")
    move_nr += 1
    print_map(map_grid)
    print("GPS:", calculate_gps(map_grid))
    print("")
