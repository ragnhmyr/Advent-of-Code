file_name="5_input_test.txt"

def get_location(seed_number, total_mapping_list):
    start_number = seed_number
    #print("SEED NUMBER:", start_number)
    for i in range(len(total_mapping_list)):
        this_mapping = total_mapping_list[i]
        #print("going to next mapping")
        #mapping_dict = {}
        for j in range(len(this_mapping)):
            dest_range = (this_mapping[j][0], this_mapping[j][0]+this_mapping[j][2])
            source_range = (this_mapping[j][1], this_mapping[j][1]+this_mapping[j][2])
            if source_range[0] <= start_number < source_range[1]:
                start_number = dest_range[0] + (start_number - source_range[0])
                #print("NEW START NUMBER", start_number)
                break
    #print("Location: ",start_number)
    return start_number

with open(file_name) as f:
    lines = f.readlines()

    #first line are the seeds
    seeds_txt = lines[0].split(":")[1].split()
    seeds_number = [int(i) for i in seeds_txt]

    #create list of list for all the different mappings
    this_map = []
    total_mapping_list = []

    for i in range(3,len(lines)): #start at line 3
        mapping_txt = lines[i].split()
        if len(mapping_txt) == 3: #to be added to that list
            mapping_number = [int(i) for i in mapping_txt]
            this_map.append(mapping_number)
        elif len(mapping_txt) == 2: #go to new list
            total_mapping_list.append(this_map)
            this_map=[]
        #remember to add the last one
        if i == len(lines)-1:
            total_mapping_list.append(this_map)
            this_map=[]

    #print(total_mapping_list)
    all_ranges = []
    for i in range(0, len(seeds_number), 2):
        all_ranges.append(range(seeds_number[i], seeds_number[i] + seeds_number[i+1]))
    print(all_ranges)

    #have to divide into lowest location
    min_location = 0
    for seed_range in all_ranges:
        for seed in seed_range:
            location = get_location(seed, total_mapping_list)
            if min_location == 0: #just to set the firsto one
                min_location = location
            elif location < min_location:
                min_location = location #set new location

    #print(locations)
    print("Min location:", min_location)

