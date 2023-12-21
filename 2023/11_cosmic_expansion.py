file_name = '11_input_test.txt'

galaxies = []
galaxy_pairs = []

class Galaxy:
    def __init__(self, row, column, gid):
        self.row = row
        self.column = column
        self.gid = gid
    def __str__(self):
        return "id: " + str(self.gid) + " row: " + str(self.row) + " column: " + str(self.column)

def getShortestPath(galaxy1, galaxy2):
    no_rows = 0
    no_columns = 0
    if galaxy1.row > galaxy2.row:
        no_rows = galaxy1.row - galaxy2.row
    elif galaxy1.row < galaxy2.row:
        no_rows = galaxy2.row - galaxy1.row
    if galaxy1.column > galaxy2.column:
        no_columns = galaxy1.column - galaxy2.column
    elif galaxy1.column < galaxy2.column:
        no_columns = galaxy2.column - galaxy1.column
    return no_rows + no_columns

#return indexes of all empty columns
#check if it has '#' in it
def getEmptyColumns(columns):
    empty_columns = []
    for i in range(len(columns)):
        if '#' not in columns[i]:
            empty_columns.append(i)
    return empty_columns

#return indexes of all empty rows
#check if it has '#' in it
def getEmptyRows(rows):
    empty_rows = []
    for i in range(len(rows)):
        if '#' not in rows[i]:
            empty_rows.append(i)
    return empty_rows

#get galaxies and also expand the space
def getGalaxiesFromTextFile(this_file_name):
    galaxies = []
    gid = 0
    with open(file_name, 'r') as f:
        rows = f.read().splitlines()
        #print("ORIGINAL ROWS")
        # theseRows = list(map(list,rows))
        # for row in theseRows:
        #     print(row)
        columns = list(map(list, zip(*rows))) #transpose the list
        empty_rows = getEmptyRows(rows)
        empty_columns = getEmptyColumns(columns)
        #first add columns
        #print("EMPTY COLUMNS", empty_columns)
        #have to increase the index of the columns list by 1 for each column added
        increase_column_index = 0
        expansion = 1
        for column_index in empty_columns:
            for _ in range(expansion):
                columns.insert(column_index+increase_column_index, ["."] * len(rows))
            #print("COLUMN INDEX", column_index)
            #rows = list(map(list, zip(*columns)))
            #print("AFTER EXPANSION")
            #for row in rows:
            #    print(row)
            increase_column_index += expansion
        #tranpose columns list to get new rows and insert the new rows at correct index
        rows = list(map(list, zip(*columns)))
        increase_row_index = 0
        for row_index in empty_rows:
            for _ in range(expansion):
                rows.insert(row_index+increase_row_index, ["."] * len(columns))
            increase_row_index += expansion
        
        for i in range(len(rows)):
            for j in range(len(columns)):
                if rows[i][j] == '#':
                    galaxies.append(Galaxy(i, j, gid))
                    gid += 1

        #now we have the new rows and columns
        #get the galaxies and save them in a list
        
    return galaxies

# set1 = {1,2}
# set2 = {2,1}

# print(set1 == set2) this is true

# list1 = [[1,2,3],[4,5,6]]
# print(list(map(list, zip(*list1))))#transpose the list

# test_input_after_expansion = [
# [".",".",".",".","#",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","#",".",".","."],
# ["#",".",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".","#",".",".",".","."],
# [".","#",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".",".",".",".","#"],
# [".",".",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".",".",".",".","."],
# [".",".",".",".",".",".",".",".",".","#",".",".","."],
# ["#",".",".",".",".","#",".",".",".",".",".",".","."],
# ]
# print("TEST ROWS")
#         for row in test_input_after_expansion:
#             print(row)
# print("ROWS VS TESTDATA", rows == test_input_after_expansion)
#         print("MY ROWS")
#         for row in rows:
#             print(row)
# print("Galaxy 5 and 9")
# print(getShortestPath(galaxies[4], galaxies[8])) #should be 9
# print("Galaxy 1 and 7")
# print(getShortestPath(galaxies[0], galaxies[6])) #should be 15
# print("Galaxy 3 and 6")
# print(getShortestPath(galaxies[2], galaxies[5])) #should be 17
# print("Galaxy 8 and 9")
# print(getShortestPath(galaxies[7], galaxies[8])) #should be 5

galaxies = getGalaxiesFromTextFile(file_name)
shortest_paths = []
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        shortest_paths.append(getShortestPath(galaxies[i], galaxies[j]))
print("SUM SHORTEST PATHS", sum(shortest_paths))
print("NUMBER OF PAIRS", len(shortest_paths))

