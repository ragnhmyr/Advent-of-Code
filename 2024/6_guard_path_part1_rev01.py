##example was wrong - said 41 but was 38

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

def main():
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



main()