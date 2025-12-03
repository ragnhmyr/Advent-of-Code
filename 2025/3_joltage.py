from itertools import combinations
from timeit import default_timer as timer

#could start with looking for 99,98 and so on and then break it
#or find first instance of 9 and then check for 9 again after that index and iterate downwards
def read_file(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines() 
        return lines

lines = read_file('3_input_test.txt')

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

def subsequences_of_length(s,length):
    subsequences = set()
    subsequences_length = combinations(s, length)
    for c in subsequences_length:
        subsequences.add(int(''.join(c)))
    return subsequences

part_2_joltage = []
start = timer()
for line in lines: 
    #part 1
    substrings = subsequences_of_2(line)
    #print("Substrings of 2 for", line, ":", substrings)
    joltage.append(max(substrings))
    #print("Max substring of 2 for", line, ":", max(substrings))
    #part 2
    subsequences_part2 = subsequences_of_length(line,12)
    part_2_joltage.append(max(subsequences_part2))
    #print("Subsequences of length for", line, ":", subsequences)

end = timer()
print("Time: ", end - start)

#print("Joltage list:", joltage)
print("Sum of Joltage part 1", sum(joltage))
print("Sum of Joltage part 2", sum(part_2_joltage))
