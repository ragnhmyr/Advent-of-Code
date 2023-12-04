import re

## Part 1
part_1_number_per_line = []
with open('1_input.txt') as f:
    for line in f:
        number_string = re.sub(r"\D","", line) #D are non-digits
        if number_string:
            part_1_number_per_line.append(int(number_string[0]+number_string[-1]))

print("PART 1", sum(part_1_number_per_line))    

## Part 2
string_to_number_dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",

}

#find first number
def find_number_start_string(line):
    first_number = ""
    for i in range(len(line)):
        start_of_line = line[0:i]
        for item in string_to_number_dict.keys():
            if item in start_of_line:
                first_number = string_to_number_dict[item]
                return first_number #return first match

#find last number 
def find_number_end_string(line):
    last_number = ""
    for i in range(len(line), -1, -1):
        end_of_line = line[i:]
        for item in string_to_number_dict.keys():
            if item in end_of_line:
                last_number = string_to_number_dict[item]
                return last_number
                
part_2_number_per_line = []
with open('1_input.txt') as f:
    for line in f:
        first_number = find_number_start_string(line)
        last_number = find_number_end_string(line)
        if first_number and last_number:
            part_2_number_per_line.append(int(first_number+last_number))

print("PART 2", sum(part_2_number_per_line))  