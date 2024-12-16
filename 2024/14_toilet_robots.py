width = 101
height = 103

#width = 11
#height = 7

#real_width = 101
#real_height = 103

start_loc = []
velocities = []
with open('14_input.txt') as f:
    for line in f:
        stripped_line = line.strip()
        loc, vel = stripped_line.split(" ")
        loc_x, loc_y = loc.split("=")[1].split(",")
        vel_x, vel_y = vel.split("=")[1].split(",")
        start_loc.append((int(loc_x),int(loc_y)))
        velocities.append((int(vel_x),int(vel_y)))

def get_grid(locations,width,height):
    #initialize grid with dots
    grid = [["." for i in range(width)] for j in range(height)]
    for i in range(len(locations)):
        x,y = locations[i]
        if grid[y][x] == ".":
            grid[y][x] = 1
        else:
            grid[y][x] += 1
    return grid

def get_loc_after_time(start_loc, velocities, seconds, width, height):
    new_loc = []
    for i in range(len(start_loc)):
        x, y = start_loc[i]
        vel_x, vel_y = velocities[i]

        # Calculate new position
        new_x = (x + vel_x * seconds) % width
        new_y = (y + vel_y * seconds) % height

        # Append wrapped position
        new_loc.append((new_x, new_y))
    return new_loc

def print_grid(grid):
    for row in grid:
        print("".join(str(x) for x in row))

#remove middle row and column
def remove_row_and_column(grid, row_id, col_id):
    grid.pop(row_id)
    for i in range(len(grid)):
        grid[i].pop(col_id)
    return grid

def count_quadrant_robot(grid):
    rows = len(grid)
    columns = len(grid[0])
    half_rows = rows // 2
    half_columns = columns // 2

    quadrants = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0
    }

    # Count robots in each quadrant
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == ".":
                continue
            if i < half_rows and j < half_columns:
                quadrants["top_left"] += grid[i][j]
            elif i < half_rows and j >= half_columns:
                quadrants["top_right"] += grid[i][j]
            elif i >= half_rows and j < half_columns:
                quadrants["bottom_left"] += grid[i][j]
            else:
                quadrants["bottom_right"] += grid[i][j]

    return quadrants

print(start_loc)
print(velocities)
grid = get_grid(start_loc,width,height)
print_grid(grid)
print("")
new_loc = get_loc_after_time(start_loc,velocities,100,width,height)
new_grid = get_grid(new_loc,width,height)
print_grid(new_grid)
col_to_remove = width//2
row_to_remove = height//2
print("")
print("Col to remove: ", col_to_remove)
print("Row to remove: ", row_to_remove)
removed_middle_grid = remove_row_and_column(new_grid,row_to_remove,col_to_remove)
print("")
print_grid(removed_middle_grid)
print("")
quadrant = count_quadrant_robot(removed_middle_grid)
tot_safety = 1
for key in quadrant:
    tot_safety *= quadrant[key]
print("Total safety: ", tot_safety)

