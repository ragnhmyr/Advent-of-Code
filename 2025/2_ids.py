def open_read_file(file_name):
    instructions = []
    with open(file_name) as f:
        for line in f:
            split_id = line.strip().split(',')
            instructions = split_id
    return instructions

##part 1
def sum_invalid_ids_part_one(instructions):
    invalid_ids = []
    for instruction in instructions:
        start,stop = instruction.split('-')
        start = int(start)
        stop = int(stop)
        for num in range(start, stop + 1):
            str_num = str(num)
            first_half = str_num[:len(str_num)//2]
            second_half = str_num[len(str_num)//2:]
            if first_half == second_half:
                invalid_ids.append(num)
    return sum(invalid_ids)

##part 2
def sum_invalid_ids_part_two(instructions):
    invalid_ids = []
    for instruction in instructions:
        start,stop = instruction.split('-')
        start = int(start)
        stop = int(stop)
        for num in range(start, stop + 1):
            str_num = str(num)
            for i in range((len(str_num)//2)+1):
                length = len(str_num)//2
                sub_string = str_num[0:i]
                if sub_string != '':
                    count_substring = str_num.count(sub_string)
                    if count_substring >= 2 and (len(sub_string) == len(str_num)/count_substring):
                        invalid_ids.append(num)
                        break
            
    return sum(invalid_ids)

instructions = open_read_file('2_input.txt')
print("Sum of invalid IDs:", sum_invalid_ids_part_two(instructions))