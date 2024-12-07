
#beware that it should go through all the numbers in the equation, not just until it finds a solution
def evaluate(target, numbers, current=0, idx=0):
    #if current matches target and we are at the end of the list, return True
    if current == target and idx == len(numbers):
        return True
    if current > target: # no need to check further if current is already greater than target
        return False
    if idx >= len(numbers): # no more numbers to check, havent found solution
        return False
    
    # Try adding and multiplying the next number
    next_number = numbers[idx]
    
    # Recurse with both operators
    return (evaluate(target, numbers, current + next_number, idx + 1) or
            evaluate(target, numbers, current * next_number, idx + 1))

def main():
    test_values = []
    equations = []
    with open('7_input.txt') as f:
        row = 0
        for line in f:
            this_line = line.strip().split(": ")
            test_values.append(int(this_line[0]))
            equation_numbers = [int(x) for x in this_line[1].split(" ")]
            equations.append(equation_numbers)
    test_values_true = []
    for i in range(len(test_values)):
        target = test_values[i]
        numbers = equations[i]
        
        if evaluate(target, numbers,numbers[0],1):
            test_values_true.append(target)
    #303876515442
    #303876515419 was too high
    print("Number of test values that can be achieved: ", len(test_values_true))
    print("Set of test values that can be achieved: ", len(set(test_values_true)))
    print("Sum total of test values: ", sum(set(test_values_true)))


main()