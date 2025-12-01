#too stupid to figure out the errors in the modulo approach, trying a more straightforward way
instructions = []
with open('1_input.txt') as f:
    for line in f:
        this_line = line.split()
        instructions.append(this_line[0])

start_dial = 50
count_zeros = 0
this_number = start_dial
count_turn = 0
for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])
    for i in range(number):
        if direction == 'R':
            this_number += 1
            if this_number > 99:
                this_number = 0
        elif direction == 'L':
            this_number -= 1
            if this_number < 0:
                this_number = 99
        if this_number == 0:
            count_zeros += 1
print("count_zeros", count_zeros)
           