all_lines = []
with open('4_input.txt') as f:
    for line in f:
        this_line = line.strip()
        all_lines.append(this_line)

word = "MAS"
word_reversed = word[::-1]
found_word = 0

number_of_columns = len(all_lines[0])
number_of_rows = len(all_lines)
this_row = 0
while this_row < number_of_rows-2:
    this_column = 0
    while this_column < number_of_columns-2:
        row1 = all_lines[this_row][this_column:this_column+3]
        row2 = all_lines[this_row+1][this_column:this_column+3]
        row3 = all_lines[this_row+2][this_column:this_column+3]
        this_column += 1
        cross1 = row1[0] + row2[1] + row3[2]
        cross2 = row1[2] + row2[1] + row3[0]
        #print(row1, row2, row3)
        if (cross1 == word or cross1 == word_reversed) and (cross2 == word or cross2 == word_reversed):
            found_word += 1
    this_row += 1

#diagonally right to left 
print("Number of MAS-crosses found: ", found_word)

