class Guard:
    def __init__(self, row, column, arrow):
        self.row = row
        self.column = column
        self.value = arrow

    def __str__(self):
        return self.value
        
    def turnRight(self):
        #arrow dict for next arrow
        arrow_dict = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        self.value= arrow_dict[self.value] #change the direction
        self.goForward() ##then move forward

    def goForward(self):
        if self.value == '^':
            self.row -= 1
        elif self.value == '>':
            self.column += 1
        elif self.value == '<':
            self.column -= 1
        elif self.value == 'v':
            self.row += 1
    
    def goBack(self):
        if self.value == '^':
            self.row += 1
        elif self.value == '>':
            self.column -= 1
        elif self.value == '<':
            self.column += 1
        elif self.value == 'v':
            self.row -= 1

class Dot:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Obstacle:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
    

class Board:
    def __init__(self, list_of_lists,guard):
        self.list_of_lists = list_of_lists
        self.guard = guard

    def __str__(self):
        result = ""
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                result += str(self.list_of_lists[i][j])
            result += '\n'  # Add a newline after each inner list
        return result

    def countTraversed(self):
        count = 0
        for i in range(len(self.list_of_lists)):
            for j in range(len(self.list_of_lists[i])):
                if self.list_of_lists[i][j].value == 'X':
                    count += 1
        return count
    
    def check_board_value(self, row, column):
        return self.list_of_lists[row][column].value
    
    def change_board_value(self, row, column, value):
        self.list_of_lists[row][column].value = value #change to 'X' for traversed board
    
    ##might have to add one if the guard does not move away from the board

def main():
    board = []
    this_guard = None
    with open('6_input_test.txt') as f:
        row = 0
        for line in f:
            this_line = line.strip()
            this_board_row = []
            for i in range(len(this_line)):
                if this_line[i] in ['^', '>', 'v', '<']:
                    this_guard = Guard(row, i, this_line[i])
                    this_board_row.append(this_guard)
                elif this_line[i] == '.':
                    this_board_row.append(Dot(this_line[i]))
                elif this_line[i] == '#':
                    this_board_row.append(Obstacle(this_line[i]))
            row += 1
            board.append(this_board_row)
    this_board = Board(board, this_guard)
    print(this_board)
    for i in range(3): #change this later to while guard.row<no_rows and guard.column<no_columns
        this_guard.goForward()
        if this_board.check_board_value(this_guard.row, this_guard.column) == '.':
            this_board.change_board_value(this_guard.row, this_guard.column, 'X')
        elif this_board.check_board_value(this_guard.row, this_guard.column) == '#':
            this_guard.goBack()
            this_guard.turnRight()
        print(this_board)
    print("Traversed paths", this_board.countTraversed())


main()
