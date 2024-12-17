def scale_up_map(original_map):
    scaled_map = []
    for row in original_map:
        scaled_row = []
        for tile in row:
            if tile == "#":
                scaled_row.extend(["#", "#"])
            elif tile == "O":
                scaled_row.extend(["[", "]"])
            elif tile == ".":
                scaled_row.extend([".", "."])
            elif tile == "@":
                scaled_row.extend(["@", "."])
        scaled_map.append(scaled_row)
    return scaled_map


def locate_player(map_grid):
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] == "@":
                return row, col


def get_dir(symbol):
    if symbol == "<":
        return (0, -1)
    if symbol == "^":
        return (-1, 0)
    if symbol == ">":
        return (0, 1)
    if symbol == "v":
        return (1, 0)


def push_box(row, col, direction, map_grid):
    # Ensure pushing a full box pair
    if map_grid[row][col] == "[" and map_grid[row][col + 1] == "]":
        next_row, next_col = row + direction[0], col + direction[1]
        next_pair_row, next_pair_col = row + direction[0], col + direction[1] + 1

        if map_grid[next_row][next_col] == "." and map_grid[next_pair_row][next_pair_col] == ".":
            map_grid[row][col], map_grid[row][col + 1] = ".", "."
            map_grid[next_row][next_col], map_grid[next_pair_row][next_pair_col] = "[", "]"
            return next_row, next_col, map_grid

    return row, col, map_grid


def move_robot_and_push(map_grid, row, col, direction):
    new_row, new_col = row + direction[0], col + direction[1]
    if map_grid[new_row][new_col] == ".":
        map_grid[new_row][new_col] = "@"
        map_grid[row][col] = "."
        return new_row, new_col, map_grid
    elif map_grid[new_row][new_col] == "#":
        return row, col, map_grid
    elif map_grid[new_row][new_col] == "[" and map_grid[new_row][new_col + 1] == "]":
        box_row, box_col, map_grid = push_box(new_row, new_col, direction, map_grid)
        if (box_row, box_col) == (new_row, new_col):
            return row, col, map_grid
        map_grid[new_row][new_col] = "@"
        map_grid[row][col] = "."
        return new_row, new_col, map_grid
    return row, col, map_grid


def print_map(map_grid):
    for row in map_grid:
        print("".join(row))


def calculate_gps(map_grid):
    gps = 0
    for row in range(len(map_grid)):
        for col in range(len(map_grid[row])):
            if map_grid[row][col] in ("[", "]"):
                gps += 100 * row + col
    return gps

# Load and scale up map
original_map = []
with open("15_input.txt") as f:
    reading_map = True
    for line in f:
        line = line.strip()
        if reading_map and line.startswith('#'):
            original_map.append(list(line))
        elif not line.startswith('#') and line:
            reading_map = False
            moves = line

scaled_map = scale_up_map(original_map)
start_row, start_col = locate_player(scaled_map)
print("start grid\n")
print_map(scaled_map)
print("")
move_nr = 0

for move in moves:
    direction = get_dir(move)
    start_row, start_col, scaled_map = move_robot_and_push(scaled_map, start_row, start_col, direction)
    print("Move nr: ", move_nr, "move symbol: ", move)
    print("")
    move_nr += 1
    print_map(scaled_map)
    print("GPS:", calculate_gps(scaled_map))
    print("")

#3154568 is too high