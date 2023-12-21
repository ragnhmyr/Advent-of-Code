file_name = '11_input.txt'

galaxies = []
galaxy_pairs = []

class Galaxy:
    def __init__(self, row, column, gid):
        self.row = row
        self.column = column
        self.gid = gid
    def __str__(self):
        return "id: " + str(self.gid) + " row: " + str(self.row) + " column: " + str(self.column)
    
    def increaseRow(self, expansion):
        self.row += expansion

    def increaseColumn(self, expansion):
        self.column += expansion

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
        columns = list(map(list, zip(*rows))) #transpose the list
        empty_rows = getEmptyRows(rows)
        empty_columns = getEmptyColumns(columns)
        expansion = 1000000

        for i in range(len(rows)):
            for j in range(len(columns)):
                if rows[i][j] == '#':
                    galaxies.append(Galaxy(i, j, gid))
                    gid += 1

        for galaxy in galaxies:
            no_of_empty_columns_before_galaxy = len([i for i in empty_columns if i < galaxy.column])
            # print("EMPTY COLUMNS",  empty_columns)
            # print("GALAXY", galaxy)
            # print("NO OF EMPTY COLUMNS BEFORE GALAXY", no_of_empty_columns_before_galaxy)
            if no_of_empty_columns_before_galaxy > 0:
                galaxy.increaseColumn(no_of_empty_columns_before_galaxy*expansion-1*no_of_empty_columns_before_galaxy) #minus 1 because we don't want to increase the column of the galaxy itself
            no_of_empty_rows_before_galaxy = len([i for i in empty_rows if i < galaxy.row])
            if no_of_empty_rows_before_galaxy > 0:
                galaxy.increaseRow(no_of_empty_rows_before_galaxy*expansion-1*no_of_empty_rows_before_galaxy) 
        
            print(galaxy)
        #now we have the new rows and columns
        #get the galaxies and save them in a list
        
    return galaxies

galaxies = getGalaxiesFromTextFile(file_name)
shortest_paths = []
for i in range(len(galaxies)-1):
    for j in range(i+1, len(galaxies)):
        shortest_paths.append(getShortestPath(galaxies[i], galaxies[j]))
print("SUM SHORTEST PATHS", sum(shortest_paths))
print("NUMBER OF PAIRS", len(shortest_paths))

#not 1112
#not 1076