import time

# Example diskmap with expected checksum 2858
diskmap = "2333133121414131402"
diskmap = "22222228282828222222282829212324252627282920" # should be 9447

#the real input
#diskmap = ""
with open('9_input.txt') as f:
    for line in f:
        diskmap = line.strip() #only one line
print(diskmap)

# Start timer
start_time = time.time()

# Parse the disk map into files and free spaces
disk_dict = {}
file_id = 0

# Parse the diskmap
for i in range(0, len(diskmap), 2):
    size = int(diskmap[i])
    space = int(diskmap[i+1]) if i+1 < len(diskmap) else 0
    disk_dict[file_id] = {"size": size, "space": space}
    file_id += 1

# Create the initial disk state
start_string = []
for key in disk_dict:
    start_string.extend([str(key)] * disk_dict[key]["size"])
    start_string.extend(["."] * disk_dict[key]["space"])

# Part 2 - Move Files
for file_id in sorted(disk_dict.keys(), reverse=True):
    file_size = disk_dict[file_id]["size"]

    # Find the leftmost free space before the file's first occurrence
    current_index = start_string.index(str(file_id))
    start_index = -1

    for i in range(current_index):
        if start_string[i:i+file_size] == ["."] * file_size:
            start_index = i
            break

    # If there's space, move the file
    if start_index != -1:
        # Clear original file blocks
        for i in range(len(start_string)):
            if start_string[i] == str(file_id):
                start_string[i] = "."

        # Place the file at the found index
        for i in range(file_size):
            start_string[start_index + i] = str(file_id)

# Calculate the checksum
checksum_part2 = sum(i * int(start_string[i]) for i in range(len(start_string)) if start_string[i].isdigit())

# Display results
print("Final Disk State:", "".join(start_string))
print("Checksum Part 2:", checksum_part2)
print("Process finished in --- %s seconds ---" % (time.time() - start_time))
#6376648986651 was correct
