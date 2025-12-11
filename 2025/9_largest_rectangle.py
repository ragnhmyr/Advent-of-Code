def read_file(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip()) for line in file.readlines()]
    return lines

def make_tuples(lines):
    tuples = []
    for line in lines:
        x,y = line.split(",")
        tuples.append((int(x),int(y)))
    return tuples 

def print_grid(coords):
    columns = max(x for x, y in coords)
    rows = max(y for x, y in coords)
    # Create a grid filled with "."
    # +1 because coordinates start at 0
    grid = [["." for _ in range(columns + 1)] for _ in range(rows + 1)]

    # Mark coordinate positions with "#"
    for x, y in coords:
        grid[y][x] = "#"

    # Print the grid
    for row in grid:
        print("".join(row))

def max_distances(coords):
    area=0
    for i in range(len(coords)-1):
        for j in range(i+1):
            x_dist = abs(coords[j][0]-coords[i][0])+1
            y_dist = abs(coords[j][1]-coords[i][1])+1
            this_area = x_dist*y_dist
            if this_area>area:
                area = this_area
    return area

def part1():
    filename = "9_input.txt"
    lines = read_file(filename)
    tuples = make_tuples(lines)
    #print_grid(tuples) #do not print with the whole input
    print("AREA", max_distances(tuples))
    
if __name__ == "__main__":
    part1()