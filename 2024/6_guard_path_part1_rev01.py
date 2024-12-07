##example was wrong - said 41 but was 38
#think it was wrong sample in part 1 of project
import copy
import time

def turnRight(value):
        # Mapping current direction to the next direction when turning right
        arrow_dict = {'^': '>', '>': 'v', 'v': '<', '<': '^'}
        return arrow_dict[value]

def checkForward(row, column, arrow):
    # Calculate the next position based on the current direction
    if arrow == '^':
        return row - 1, column
    elif arrow == '>':
        return row, column + 1
    elif arrow == '<':
        return row, column - 1
    elif arrow == 'v':
        return row + 1, column
    print(f"Unexpected direction in move: {arrow}")
    return row, column  # Fallback to current position

def checkBackward(row, column, arrow):
    # Calculate the next position based on the current direction
    if arrow == '^':
        return row + 1, column
    elif arrow == '>':
        return row, column - 1
    elif arrow == '<':
        return row, column + 1
    elif arrow == 'v':
        return row - 1, column
    print(f"Unexpected direction in move: {arrow}")
    return row, column  # Fallback to current position

def main_part_1():
    board = []
    initial_guard_row = 0
    initial_guard_column = 0
    with open('6_input.txt') as f:
        row = 0
        for line in f:
            this_line = line.strip()
            this_board_row = []
            for i in range(len(this_line)):
                if this_line[i] in ['^',"v",">","<"]:
                    initial_guard_row = row
                    initial_guard_column = i
                this_board_row.append(this_line[i])
            row+=1
            board.append(this_board_row)
    no_rows = len(board)
    no_columns = len(board[0])
    visited_positions = [(initial_guard_row, initial_guard_column)]
    this_arrow = board[initial_guard_row][initial_guard_column]
    new_row, new_column = checkForward(initial_guard_row, initial_guard_column, this_arrow)
    while (new_row >= 0 and new_row < no_rows and new_column >= 0 and new_column < no_columns):
        if board[new_row][new_column] == '#':
            new_row, new_column = checkBackward(new_row, new_column, this_arrow)
            this_arrow = turnRight(this_arrow)
        else:
            visited_positions.append((new_row, new_column))
            new_row, new_column = checkForward(new_row, new_column, this_arrow)

    set_of_visited_positions = set(visited_positions)
    for places in set_of_visited_positions:
        board[places[0]][places[1]] = 'X'
    for line in board:
        print("".join(line))
    #print("Visited positions", visited_positions)
    #print("set of Visited positions", visited_positions)
    print("Distinct positions: ", len(set_of_visited_positions))

def main_part_2():
    board = []
    initial_guard_row = 0
    initial_guard_column = 0
    #brute force - add the obstacles one by one and check if the guard can reach the end
    #can simplify it a bit by only adding obstacles in the path of the guard andn not to cells where the guard never reaches anyway
    with open('6_input.txt') as f:
        row = 0
        for line in f:
            this_line = line.strip()
            this_board_row = []
            for i in range(len(this_line)):
                if this_line[i] in ['^',"v",">","<"]:
                    initial_guard_row = row
                    initial_guard_column = i
                this_board_row.append(this_line[i])
            row+=1
            board.append(this_board_row)
    no_rows = len(board)
    no_columns = len(board[0])
    visited_positions = [(initial_guard_row, initial_guard_column)]
    this_arrow = board[initial_guard_row][initial_guard_column]
    new_row, new_column = checkForward(initial_guard_row, initial_guard_column, this_arrow)
    #assuming that 
    while (new_row >= 0 and new_row < no_rows and new_column >= 0 and new_column < no_columns):
        if board[new_row][new_column] == '#':
            new_row, new_column = checkBackward(new_row, new_column, this_arrow)
            this_arrow = turnRight(this_arrow)
        else:
            visited_positions.append((new_row, new_column))
            new_row, new_column = checkForward(new_row, new_column, this_arrow)

    set_of_visited_positions = set(visited_positions)
    ##one by one add an obstacle to the cells that are visited and check for infinite loops
    ##assuming that if a position has been visited more than 3 times it is an infinite loop
    #remove the initial guard position from the set 
    possible_obstacle_positions = set_of_visited_positions - {(initial_guard_row, initial_guard_column)} ##remove the guard position from the set to not set an obstacle there
    infinite_loops = 0
    for obstacle_position in possible_obstacle_positions:
        new_board = copy.deepcopy(board)
        new_board[obstacle_position[0]][obstacle_position[1]] = 'O'
        # for line in new_board:
        #     print("".join(line))
        visited_positions = [(initial_guard_row, initial_guard_column)]
        this_arrow = new_board[initial_guard_row][initial_guard_column]
        new_row, new_column = checkForward(initial_guard_row, initial_guard_column, this_arrow)
        guard_comes_out = False
        while (guard_comes_out == False):
            if (new_row <0 or new_row >= no_rows or new_column < 0 or new_column >= no_columns):
                guard_comes_out = True
            elif new_board[new_row][new_column] in ['#','O']:
                new_row, new_column = checkBackward(new_row, new_column, this_arrow)
                this_arrow = turnRight(this_arrow)
            else:
                visited_positions.append((new_row, new_column))
                new_row, new_column = checkForward(new_row, new_column, this_arrow)
            if visited_positions.count((new_row, new_column)) > 4:
                infinite_loops += 1
                break
        new_visited_set = set(visited_positions)
        for places in new_visited_set:
            new_board[places[0]][places[1]] = 'X'
        # for line in new_board:
        #     print("".join(line))
    #print("Visited positions", visited_positions)
    #print("set of Visited positions", visited_positions)
    print("Distinct positions: ", len(set_of_visited_positions))
    print("Infinite loops: ", infinite_loops)

start_time = time.time()
main_part_2()
print("Process finished --- %s seconds ---" % (time.time() - start_time))
#part 2 worked in 25 mins haha - checking if guard is in same place 10 times, probably a little less time now.
#should be enough to check if guard is in same place more than 4 times - one in each direction