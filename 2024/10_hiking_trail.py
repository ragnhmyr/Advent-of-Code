map = []
with open('10_input.txt') as f:
    for line in f:
        map.append([int(x) for x in line.strip()]) #only one line
no_rows = len(map)
no_columns = len(map[0])
print(map)

#location as a tuple(row,column)
#neighbours as a list of tuples where valid neighbours are neighbouring cells that exist on the grid
def find_valid_neighbours(location,no_total_rows,no_columns):
    valid_neighbours = []
    this_row = location[0]
    this_column = location[1]
    #up, right, down, left
    next_locations = [(this_row-1,this_column),(this_row,this_column+1),(this_row+1,this_column),(this_row,this_column-1)]
    for next_location in next_locations:
        if next_location[0] >= 0 and next_location[0] < no_total_rows and next_location[1] >= 0 and next_location[1] < no_columns:
            valid_neighbours.append(next_location)
    return valid_neighbours

def check_if_neighbour_is_on_trail(this_location,neighbour_location,map):
    this_value = map[this_location[0]][this_location[1]]
    neighbour_value = map[neighbour_location[0]][neighbour_location[1]]
    return neighbour_value == this_value + 1
    
#find the start values at 0 
#then go through the neigbhours.
#if it gets to 9, then it is the end, path is increased by 1
#else go to next neighbour
#valid paths is a path that goes from 0 to 9 with only one increasing value

def count_hiking_trails(map, start_loc, no_rows, no_columns):
    # If reached the end of the trail return 1 as we found a valid path
    #print("Looking at value",map[start_loc[0]][start_loc[1]],"at location",start_loc)
    if map[start_loc[0]][start_loc[1]] == 9:
        #print("Found the end of a path, returning 9")
        return 1

    total_paths = 0
    neighbours = find_valid_neighbours(start_loc, no_rows, no_columns)
    for neighbour in neighbours:
        #print("Found a neighbour at ",neighbour, "neighbour value is",map[neighbour[0]][neighbour[1]])
        if check_if_neighbour_is_on_trail(start_loc, neighbour, map):
            #print("Neighbour is on the trail")
            # Continue searching from the valid neighbour
            total_paths += count_hiking_trails(map, neighbour, no_rows, no_columns)

    return total_paths

def count_hiking_trails_part1(map, start_loc, no_rows, no_columns):
    to_visit = [start_loc]
    reached_end_points = set()

    while to_visit:
        current_loc = to_visit.pop()
        current_value = map[current_loc[0]][current_loc[1]]

        if current_value == 9:
            reached_end_points.add(current_loc)
            continue

        for neighbour in find_valid_neighbours(current_loc, no_rows, no_columns):
            if map[neighbour[0]][neighbour[1]] == current_value + 1:
                to_visit.append(neighbour)

    return len(reached_end_points)

def main(map,no_rows,no_columns):
    start_locations = []
    for i in range(no_rows):
        for j in range(no_columns):
            if map[i][j] == 0:
                start_locations.append((i,j))
    ranks_per_start_1 = []
    ranks_per_start_2 = []
    for start_loc in start_locations:
        #print("*******")
        #print("Checking start location",start_loc)
        ranks_per_start_1.append(count_hiking_trails_part1(map,start_loc,no_rows,no_columns))
        ranks_per_start_2.append(count_hiking_trails(map,start_loc,no_rows,no_columns))
    print("part 1 ranks per start: ", ranks_per_start_1)
    print("part 1 ranks sum: ", sum(ranks_per_start_1))
    print("part 2 ranks per start", ranks_per_start_2)
    print("part 2 sum of ranks",sum(ranks_per_start_2))


main(map,no_rows,no_columns)
