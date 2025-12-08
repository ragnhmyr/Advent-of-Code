import copy 

def read_file(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip()) for line in file.readlines()]
    return lines

def find_start_position(line):
    for i in range(len(line)):
        if line[i] == "S":
            return i
        
def print_char_list(list):
    for elem in list:
        text = "".join(str(x) for x in elem)
        print(text)
    print("\n")
    
def count_total_splits(char_list):
    #if `|` is above and to both sides of '^' count the split
    total_splits = 0
    for i in range(len(char_list)):
        for j in range(len(char_list[i])):
            if char_list[i][j] == "^" and (char_list[i][j-1] == char_list[i][j+1] == char_list[i-1][j] == "|"):
                total_splits += 1 
    return total_splits

def part1():
    filename = "7_input_test.txt"
    lines = read_file(filename)
    start_index = find_start_position(lines[0])
    char_list = [list(line) for line in lines[1:]]
    char_list[0][start_index]="|"
    print("Len char list", len(char_list))
    for i in range(1,len(char_list)):
        for j in range(len(char_list[i])):
            if char_list[i][j] == "^" and char_list[i-1][j] == "|" and j in range(1,len(char_list[i])-1): #assumes that ^ cant be next to another ^ 
                char_list[i][j-1] = "|"
                char_list[i][j+1] = "|"
            elif char_list[i][j] == "." and char_list[i-1][j] == "|":
                char_list[i][j] = "|"
    print_char_list(char_list)
    print("Total splits ", count_total_splits(char_list))
    return char_list

def part2(char_list):
    new_char_list = [[0 if x == "|" else x for x in sublist] for sublist in char_list]
    print(new_char_list)
    print_char_list(new_char_list)
    for i in range(1,len(char_list)):
        for j in range(1,len(char_list[i])-1):
            if char_list[i][j]=="|" and (char_list[i][j+1] or char_list[i][j-1] == "^"):
                new_char_list[i][j] +=1
                print_char_list(new_char_list)
            if char_list[i-1][j] == "|" and char_list[i][j] not in [".","^"]:
                new_char_list[i][j] +=1
                print_char_list(new_char_list)
    print_char_list(new_char_list)

if __name__ == "__main__":
    part2_start = part1()
    part2(part2_start)