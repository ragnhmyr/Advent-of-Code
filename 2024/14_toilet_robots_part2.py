width = 101
height = 103

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

def return_grid_only_shapes(grid):
    result = []
    for row in grid:
        new_row = ["X" if cell != "." else "." for cell in row]
        result.append("".join(new_row))
    return "\n".join(result)


## search in output after many XXXX after one another
new_text_file = open("14_output.txt", "w")
for i in range(5000,10000):
    new_loc = get_loc_after_time(start_loc,velocities,i,width,height)
    new_grid = get_grid(new_loc,width,height)
    new_text_file.write("\nAfter " + str(i) + " seconds:\n")
    new_text_file.write(return_grid_only_shapes(new_grid))
new_text_file.close()

