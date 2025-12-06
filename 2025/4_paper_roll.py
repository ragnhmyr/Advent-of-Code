def read_roll_file(filename: str) -> list[str]:
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return lines

def main():
    file_name = '4_input_test.txt'
    lines = read_roll_file(file_name)
    no_columns = len(lines[0])
    print("Number of columns:", no_columns)
    total_valid_positions = 0
    new_lines = lines.copy()
    for i in range(len(lines)):
        for j in range(no_columns):
            count_adjacent_rolls = 0
            adjacent_positions = [(i-1, j-1), (i-1, j), (i-1, j+1),
                                  (i, j-1),             (i, j+1),
                                  (i+1, j-1), (i+1, j), (i+1, j+1)]
            for x, y in adjacent_positions: #find valid positions
                if 0 <= x < len(lines) and 0 <= y < no_columns:
                    if lines[x][y] == '@':
                        print("Adjacent roll found at:", (x, y))
                        print("Adjacent roll position value:", lines[x][y])
                        count_adjacent_rolls += 1
                        if count_adjacent_rolls >= 4:
                            #j+=1
                            break
            #checking if valid position - then it is a valid position for forklift
            if count_adjacent_rolls < 4:
                new_lines[i][j] = 'X'
                print("Found valid forklift position at:", (i, j))
                print(new_lines)
            total_valid_positions += 1
            
    print(new_lines)
    print(f"Total valid forklift positions: {total_valid_positions}")

if __name__ == "__main__":
    main()