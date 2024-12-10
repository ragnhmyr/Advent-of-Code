import time

diskmap = "2333133121414131402" # this is the test input
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

start_string = ""
only_numbers = [str(key) for key in disk_dict for _ in range(int(disk_dict[key]["size"]))]
only_numbers.reverse() #reverse the numbers to find which one to insert first
for key in disk_dict:
    start_string += disk_dict[key]["size"]*str(key) + disk_dict[key]["space"]*"."
        
string_list = list(start_string)
length_stringlist = len(string_list)
empty_spaces = string_list.count(".")
moved_items = 0
last_item = -1
while moved_items != total_spaces:
    removed_item = string_list.pop() # remove the last item from the list
    if "." in string_list:
        first_index = string_list.index(".")
        string_list[first_index] = only_numbers[moved_items] 
    #print("".join(string_list))
    moved_items += 1

print("".join(string_list))
checksum = 0
for i in range(len(string_list)):
    checksum += i*int(string_list[i])
#90427061447 was too low - forgot to take into account that numbers have more than one digit above 9
#17548852145461 was too high
print("Checksum:", checksum)
print("Process finished --- %s seconds ---" % (time.time() - start_time)) # part 1 took 65 seconds