instructions = []
with open('2_input_test.txt') as f:
    for line in f:
        split_id = line.strip().split(',')
        instructions = split_id

invalid_ids = []
for instruction in instructions:
    start,stop = instruction.split('-')
    start = int(start)
    stop = int(stop)
    for num in range(start, stop + 1):
        str_num = str(num)
        first_half = str_num[:len(str_num)//2]
        second_half = str_num[len(str_num)//2:]
        #print(f'Checking ID: {num}, First half: {first_half}, Second half: {second_half}')
        if first_half == second_half:
            invalid_ids.append(num)
            #print(f'\nInvalid ID found: {num}')

print("Sum of invalid IDs:", sum(invalid_ids))