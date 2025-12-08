
import numpy as np

def read_math_homework_file(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip()).split() for line in file.readlines()]
    return lines

def part1():
    filename = "6_input_test.txt"
    lines = read_math_homework_file(filename)
    transposed = np.transpose(lines)
    print(transposed)

if __name__ == "__main__":
    part1()