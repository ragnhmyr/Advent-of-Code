instructions = []
with open('1_input.txt') as f:
    for line in f:
        this_line = line.split()
        instructions.append(this_line[0])

start_dial = 50
count_zeros = 0
this_number = start_dial
for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])
    if direction == 'R':
        this_number += number % 100
        if this_number > 99:
            this_number -= 100
        if this_number == 0:
            count_zeros += 1
        
    if direction == 'L':
        this_number -= number % 100
        if this_number < 0:
            this_number += 100
        if this_number == 0:
            count_zeros += 1
    print("This number is", this_number)

print(f'Count zeros: {count_zeros}')
           
