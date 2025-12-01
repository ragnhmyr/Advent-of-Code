#not working properly
instructions = []
with open('1_input_test.txt') as f:
    for line in f:
        this_line = line.split()
        instructions.append(this_line[0])

#instructions = instructions[:110]  # For testing with a smaller set

start_dial = 50
this_number = start_dial
count_zeros = 0
turn = 0
for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])
    previous_number = this_number
    if direction == 'R':
        this_number += number
    elif direction == 'L':
        this_number -= number
    quotient,modulo = divmod(this_number,100)
    print("\nTURN ", turn)
    print("INSTRUCTION", instruction)
    print("QUOTIENT", quotient)
    print("MODULO", modulo)
    print("PREVIUS NUMBER", previous_number)
    if modulo == 0 or (quotient != 0 and previous_number!=0) or (previous_number == 0 and modulo == 0) or (previous_number == modulo):
        added_zeros = max(1,abs(quotient))
        print("ADDING ZEROS:", added_zeros)
        count_zeros += added_zeros
    # elif quotient != 0:
    #     count_zeros += abs(quotient)
    if previous_number == 0 and modulo == 0:
        print("BOTH ARE ZERO")
    this_number = modulo
    print("This number is", this_number)
    print(f'Count zeros: {count_zeros}')
    turn +=1 

print(f'Count zeros: {count_zeros}')
