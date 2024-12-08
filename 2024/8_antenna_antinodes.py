
# input is row and column of each antenna, need to find the antinode locations
def find_antinode_locations(location1,location2,max_row,max_column): 
    # Placeholder for the function implementation
    row1, column1 = location1
    row2, column2 = location2
    dist_row = row2 - row1
    dist_column = column2 - column1
    first_antinode = (row1 - dist_row, column1 - dist_column)
    second_antinode = (row2 + dist_row, column2 + dist_column)
    valid_antinodes = []
    if first_antinode[0] >= 0 and first_antinode[0] < max_row and first_antinode[1] >= 0 and first_antinode[1] < max_column:
        valid_antinodes.append(first_antinode)
    if second_antinode[0] >= 0 and second_antinode[0] < max_row and second_antinode[1] >= 0 and second_antinode[1] < max_column:
        valid_antinodes.append(second_antinode)
    return valid_antinodes


#should really check if the character is either a letter or digit, but seems like the input only has dots and letter/digits
#so only check that the character is not a dot
def main():
    no_rows = 0
    no_columns = 0
    location_dict = {} #dictionary with the location of each antenna
    grid_to_draw = [] #grid to draw the antinode locations
    with open('8_input_test.txt') as f:
        for line in f:
            this_line = line.strip()
            no_columns = len(this_line)
            grid_to_draw.append(this_line)
            for i in range(no_columns):
                if this_line[i] != ".":
                    if this_line[i] in location_dict:
                        location_dict[this_line[i]].append((no_rows,i))
                    else:
                        location_dict[this_line[i]] = [(no_rows,i)]
            no_rows+=1
    antinode_location=[]
    for key in location_dict:
        if len(location_dict[key]) >= 2: # only compute antinodes if there are at least one antenna pair
            for i in range(len(location_dict[key])):
                for j in range(i+1,len(location_dict[key])):
                    #print("Checking antinodes for antenna ", key, " at locations ", location_dict[key][i], " and ", location_dict[key][j])
                    antinode_location.extend(find_antinode_locations(location_dict[key][i],location_dict[key][j],no_rows,no_columns)) #Extend appends individual elements instead of the list itself
    
    #create set to get all the unique values
    unique_locations = set(antinode_location)
    # Convert grid_to_draw rows to lists of characters to be able to change the characters
    grid_to_draw = [list(row) for row in grid_to_draw]
    for location in unique_locations:
        grid_to_draw[location[0]][location[1]] = "#"
    #print(location_dict)
    print("Grid with antinodes: ", grid_to_draw)
    print("Number of unique antinode locations: ", len(unique_locations))

main()