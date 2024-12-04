
all_lines = []
with open('4_input.txt') as f:
    for line in f:
        this_line = line.strip()
        all_lines.append(this_line)

word = "XMAS"
word_reversed = word[::-1]
found_word = 0

#horizontally
for line in all_lines:
    found_word += line.count(word) + line.count(word_reversed) #check both ways

#vertically
for i in range(len(all_lines[0])):
    column = ""
    for j in range(len(all_lines)):
        column += all_lines[j][i]
    found_word += column.count(word) + column.count(word_reversed) #check both ways

#diagonally left to right
#get all diagonals in a list - must have same amount of columns in every row
#function to concatenate all diagonals in a list from left to right
#could use numpy to get the diagonals.
def get_diagonals(list_of_lines): 
    number_of_columns = len(list_of_lines[0])
    number_of_rows = len(list_of_lines)
    left_to_right_diagonals = []

    # Get diagonals starting from each column in the first row
    for start_col in range(number_of_columns):
        col = start_col
        row = 0
        diagonal = ""
        while col < number_of_columns and row < number_of_rows:
            diagonal += list_of_lines[row][col]
            col += 1
            row += 1
        left_to_right_diagonals.append(diagonal)
    
    # Get diagonals starting from each row in the first column
    for start_row in range(1, number_of_rows):  # Start from row 1 to avoid duplicating the top-left diagonal
        col = 0
        row = start_row
        diagonal = ""
        while col < number_of_columns and row < number_of_rows:
            diagonal += list_of_lines[row][col]
            col += 1
            row += 1
        left_to_right_diagonals.append(diagonal)
    return left_to_right_diagonals

left_to_right_diagonals = get_diagonals(all_lines)
for diagonal in left_to_right_diagonals:
    found_word += diagonal.count(word) + diagonal.count(word_reversed) #check both ways

#reverse the original list and do the same as above 
reverse_all_lines = []
for line in all_lines:
    reverse_all_lines.append(line[::-1])

right_to_left_diagonals = get_diagonals(reverse_all_lines)
for diagonal in right_to_left_diagonals:
    found_word += diagonal.count(word) + diagonal.count(word_reversed) #check both ways

#can do the same as the right one just reverse the list in the beginning, I think 

#diagonally right to left 
print("Number of XMAS words found: ", found_word)

