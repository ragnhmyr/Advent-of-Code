import time

diskmap = '23222120202525282820202020272722212121' # this is the test input
start_time = time.time()
# diskmap = ""
# with open('9_input.txt') as f:
#     for line in f:
#         diskmap = line.strip() #only one line
# print(diskmap)
disk_dict = {}
id = 0
total_spaces = 0
for i in range(0, len(diskmap), 2):
    #might be an odd number where the last digit has no space
    size = diskmap[i]
    space = diskmap[i+1] if i+1 < len(diskmap) else 0  # Default space to 0 if last item has no space
    #print("id:", id, "diskmap[i]:", size, "diskmap[i+1]:", space)
    disk_dict[id] = {"size": int(size), "space": int(space)}
    total_spaces += int(space)
    id += 1

start_string = []
only_numbers = [str(key) for key in disk_dict for _ in range(int(disk_dict[key]["size"]))]
only_numbers.reverse() #reverse the numbers to find which one to insert first
for key in disk_dict:
    # Add numbers based on size
    start_string.extend([str(key)] * int(disk_dict[key]["size"]))
    # Add empty spaces (.) based on space
    start_string.extend(["."] * int(disk_dict[key]["space"]))
        
length_stringlist = len(start_string)
empty_spaces = start_string.count(".")
moved_items = 0
last_item = -1
while moved_items != total_spaces:
    removed_item = start_string.pop() # remove the last item from the list
    if "." in start_string:
        first_index = start_string.index(".")
        start_string[first_index] = only_numbers[moved_items] 
    #print("".join(string_list))
    moved_items += 1

print("".join(start_string))
checksum_part1 = 0
for i in range(len(start_string)):
    checksum_part1 += i*int(start_string[i])
#90427061447 was too low - forgot to take into account that numbers have more than one digit above 9
#17548852145461 was too high - forgot to take into account that numbers have more than one digit in the string list
#6349606724455 correct - 15 sec
print("Checksum part 1:", checksum_part1)
print("Part 1 Process finished --- %s seconds ---" % (time.time() - start_time)) # part 1 took 65 seconds


start_time_2 = time.time()
only_numbers_2 = [[str(key)] * int(disk_dict[key]["size"]) for key in disk_dict]
only_numbers_2.reverse()
print(only_numbers_2)
start_string_2 = []
for key in disk_dict:
    # Add numbers based on size
    key_list = [str(key)] * int(disk_dict[key]["size"])
    # Add empty spaces (.) based on space
    space_list = ["."] * int(disk_dict[key]["space"])
    start_string_2.append([key_list, space_list])

print(start_string_2)
for i in range(len(only_numbers_2)):
    size_this_list = len(only_numbers_2[i])
    list_looking_at = only_numbers_2[i]
    #print("List looking at:", list_looking_at)
    #print("Size this list:", size_this_list)
    for j in range(len(start_string_2)):
        space_this_list = start_string_2[j][1].count(".")
        #print("Checking if it can be replaced with:", start_string_2[j][1])
        #print("Space this list:", space_this_list)
        if space_this_list >= size_this_list:
            replacements = 0
            for k in range(len(start_string_2[j][1])):
                if start_string_2[j][1][k] == "." and replacements < size_this_list:
                    #print(f"Replacing {start_string_2[j][1][k]} with {only_numbers_2[i][0]}")
                    start_string_2[j][1][k] = only_numbers_2[i][0]
                    replacements += 1

            # Use an extra field to mark completion
            if replacements == size_this_list:
                #print(f"Completed replacements for: {start_string_2[j][0]}")
                start_string_2[-1-i][0] = ["." for _ in range(size_this_list)]  # Clear the corresponding number list
                break 
#print("****")
print(start_string_2)
result_list = [item for sublist in start_string_2 for inner_list in sublist for item in inner_list]
print(result_list)
checksum_part2 = 0
#might have to be careful of id's and "."
for i in range(len(result_list)):
    if result_list[i] != ".":
        checksum_part2 += i*int(result_list[i])
#8504654861152 is too high
print("Checksum part 2:", checksum_part2)
print("Part 2 Process finished --- %s seconds ---" % (time.time() - start_time_2)) # part 1 took 65 seconds

