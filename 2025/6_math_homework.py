
import numpy as np
import math

def read_math_homework_file(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip()).split() for line in file.readlines()]
    return lines

def read_math_homework_file_part2(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip("\n")) for line in file.readlines()]
    return lines

def part1():
    filename = "6_input.txt"
    lines = read_math_homework_file(filename)
    transposed = np.transpose(lines)
    sum_all = 0
    for expression in transposed:
        if expression[-1] == "+":
            sum_all += sum(int(a) for a in expression[0:len(expression)-1])
        elif expression[-1] == "*":
            sum_all += math.prod(int(a) for a in expression[0:len(expression)-1])
    print("Total sum is", sum_all)

def process_block(block):
    """
    block: list of rows, e.g.
    [
        ['1',' ',' ','*'],
        ['2','4',' ',' '],
        ['3','5','6',' '],
    ]
    """
    # 1. Find operator anywhere in the block (typically in the first row, last col)
    op = None
    for row in block:
        for ch in row:
            if ch in '+*':
                op = ch
                break
        if op is not None:
            break

    if op is None:
        raise ValueError("No + or * operator found in block")

    # 2. Collect numbers row-wise
    numbers = []
    for row in block:
        digits = [ch for ch in row if ch.isdigit()]  # ignore spaces and operators
        if digits:
            num = int(''.join(digits))
            numbers.append(num)

    if not numbers:
        raise ValueError("No numbers found in block")

    # 3. Apply the operator
    if op == '*':
        return math.prod(numbers)   # e.g. 1 * 24 * 356
    else:  # op == '+'
        return sum(numbers)        # e.g. 369 + 248 + 8

def solve(transposed):
    results = []
    block = []

    for row in transposed:
        if all(c == ' ' for c in row):
            results.append(process_block(block))
            block = []
        else:
            block.append(row)

    if block:
        results.append(process_block(block))

    return results

def part2():
    filename = "6_input.txt"
    lines = read_math_homework_file_part2(filename)
    list_char = [list(line) for line in lines]
    transposed = np.transpose(list_char)
    result = solve(transposed)
    sum_all = sum(result)
    print("Total sum is", sum_all)

if __name__ == "__main__":
    #part1()
    part2()