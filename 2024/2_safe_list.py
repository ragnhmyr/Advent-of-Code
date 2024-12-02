all_lines = []
with open('2_input.txt') as f:
    for line in f:
        this_line = line.strip().split()
        numbers = list(map(int, this_line)) #convert all to numbers
        all_lines.append(numbers)

## PART 1
# number_safe_lists = 0
# for i in range(len(all_lines)):
#     this_list = all_lines[i]
#     diff = []
#     for j in range(len(this_list)-1):
#         one_diff = this_list[j+1] - this_list[j]
#         if abs(one_diff)<=3 and one_diff != 0:
#             diff.append(one_diff)
#         else:
#             break
#     if len(diff) == len(this_list)-1: #all differences are 3 or less and not euqal to 0
#         if all(x < 0 for x in diff) or all(x > 0 for x in diff):
#             number_safe_lists += 1

##PART 2
def check_list(this_list):
    diff = []
    for j in range(len(this_list)-1):
        one_diff = this_list[j+1] - this_list[j]
        if abs(one_diff)<=3 and one_diff != 0:
            diff.append(one_diff)
        else:
            break
    if len(diff) == len(this_list)-1: #all differences are 3 or less and not euqal to 0
        if all(x < 0 for x in diff) or all(x > 0 for x in diff):
            return True
    return False

#get all the permutations and check that list
def permute_list(this_list):
    for i in range(len(this_list)):
        new_list = this_list.copy()
        new_list.pop(i)
        if check_list(new_list):
            return True
    return False

number_safe_lists = 0
print(all_lines)
for i in range(len(all_lines)):
    this_list = all_lines[i]
    print(this_list)
    if check_list(this_list):
        number_safe_lists += 1
    else:
        if permute_list(this_list):
            number_safe_lists += 1


print("number of safe lists", number_safe_lists)


