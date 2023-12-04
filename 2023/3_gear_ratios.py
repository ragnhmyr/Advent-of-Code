import re

#groups
#match_digits = re.findall(r"(\D+)(\d+)", line) #D is any non-digit character, #d is any digit character
#match_symbols_not_dot = re.findall(r"([\.\w\s]+)([^\.\w\s]+)", line) #first group: dot or any word character or space, second group: any that is not in the first group (ie. symbols)

# match_digits = re.findall(r"\d+", line) #D is any non-digit character, #d is any digit character
# match_symbols_not_dot = re.findall(r"[^\.\w\s]+", line) #any symbol that is not a dot or any word character or space

# gets first match
# match_digits = re.search(r"[\d]+", line) #D is any non-digit character, #d is any digit character
# match_symbols_not_dot = re.search(r"[^\.\w\s]+", line) #any symbol that is not a dot or any word character or space

valid_numbers = []

symbols = {}

file_name = '3_input.txt'

#PART 1

with open(file_name) as f:
    line_number = 0
    #get all the symbols in a dictionary
    for line in f:
        symbols_array = []
        match_symbols_not_dot = re.finditer(r"[^\.\w\s]", line) #any symbol that is not a dot or any word character or space
        
        for match in match_symbols_not_dot:
            symbols_array.append(match.start()) #save all the indexes of symbols
        
        if len(symbols_array)>0:
            symbols[line_number]=symbols_array #get all the indexes of symbols in each line

        line_number+=1

#get all numbers and check if they are valid - index of symbol -+1 or in index of string either same line or before/after
with open(file_name) as g:    
    line_number = 0
    for line in g: 
        match_digits = re.finditer(r"[\d]+", line) #D is any non-digit character, #d is any digit character
        for match in match_digits:
            number = int(match.group())
            index_list = list(range(match.start()-1, match.end() + 1))
            for i in range(line_number-1,line_number+2): #plus 2 because range is exclusive
                if i in symbols.keys():
                    if any(x in symbols[i] for x in index_list):
                        valid_numbers.append(number)
        line_number+=1

print("sum of valid numbers", sum(valid_numbers)) 

#PART 2

# gears ={
#     line_number: {index: [neighbor1,neighboer2]}
# }
number_adjacent_gear_multiplied = []
gears = {}
with open(file_name) as f:
    line_number = 0
    #get all the symbols in a dictionary
    for line in f:
        match_gear_symbols = re.finditer(r"\*", line) #any symbol that is not a dot or any word character or space
        gears[line_number] = {}
        for match in match_gear_symbols:
            gears[line_number][match.start()]=[] #get all the indexes of symbols in each line
        line_number+=1

with open(file_name) as g:    
    line_number = 0
    for line in g: 
        match_digits = re.finditer(r"[\d]+", line) #D is any non-digit character, #d is any digit character
        for match in match_digits:
            number = int(match.group())
            index_list = list(range(match.start()-1, match.end() + 1))
            for i in range(line_number-1,line_number+2): #plus 2 because range is exclusive
                if i in gears.keys():
                    #if number is neighbour to a gear
                    for index in index_list:
                        if index in gears[i].keys():
                            gears[i][index].append(number)
        line_number+=1

#check that gears have exactly 2 neighbours and multiply those numbers
for line in gears:
    for index in gears[line]:
        if len(gears[line][index])==2:
            number_adjacent_gear_multiplied.append(gears[line][index][0]*gears[line][index][1])

print("sum of numbers multiplied", sum(number_adjacent_gear_multiplied))
