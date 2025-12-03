from itertools import combinations
from timeit import default_timer as timer

#could start with looking for 99,98 and so on and then break it
#or find first instance of 9 and then check for 9 again after that index and iterate downwards
def read_file(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines() 
        return lines

lines = read_file('3_input.txt')

joltage = []

#find all subsequences, but we only want the two length ones, lof of computation
def all_subsequences(s):
    out = set()
    for r in range(1, len(s) + 1):
        for c in combinations(s, r):
            out.add(''.join(c))
    return sorted(out)

#return only the maximum two digit subsequence
def subsequences_of_2(s):
    subsequences = set()
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            subsequences.add(int(s[i] + s[j]))
    return subsequences

#only works if not too long string
def subsequences_of_length(s,length):
    #subsequences = set()
    subsequences_length = combinations(s, length)
    return subsequences_length

def find_largest_subsequence(original_string: str, target_length: int) -> str:
    number_of_deletions_allowed = len(original_string) - target_length
    chosen_digits_stack = []

    for current_digit in original_string:
        # Remove smaller digits from the stack if the current digit is larger
        # and we still have deletions available
        while (number_of_deletions_allowed > 0 
               and chosen_digits_stack 
               and chosen_digits_stack[-1] < current_digit):
            chosen_digits_stack.pop()
            number_of_deletions_allowed -= 1

        chosen_digits_stack.append(current_digit)

    # If we still have deletions allowed, remove digits from the end
    if number_of_deletions_allowed > 0:
        chosen_digits_stack = chosen_digits_stack[:-number_of_deletions_allowed]

    return "".join(chosen_digits_stack)

part_2_joltage = []
start = timer()
for line in lines: 
    #part 1
    substrings = subsequences_of_2(line)
    joltage.append(max(substrings))
    #part 2
    biggest_number = int(find_largest_subsequence(line,12))
    part_2_joltage.append(biggest_number)

end = timer()
print("Time: ", end - start)
print("Sum of Joltage part 1", sum(joltage))
print("Sum of Joltage part 2", sum(part_2_joltage))
