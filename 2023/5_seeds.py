file_name="5_input.txt"

def get_location(seed_number, total_mapping_list):
    start_number = seed_number
    print("SEED NUMBER:", start_number)
    for i in range(len(total_mapping_list)):
        this_mapping = total_mapping_list[i]
        print("going to next mapping")
        mapping_dict = {}
        for j in range(len(this_mapping)):
            dest_range = (this_mapping[j][0], this_mapping[j][0]+this_mapping[j][2])
            source_range = (this_mapping[j][1], this_mapping[j][1]+this_mapping[j][2])
            mapping_dict[source_range] = dest_range

        for source_range, dest_range in mapping_dict.items():
            if source_range[0] <= start_number < source_range[1]:
                start_number = dest_range[0] + (start_number - source_range[0])
                print("NEW START NUMBER", start_number)
                break
        # total_dest = []
        # total_source = []
        # print("THIS MAPPING", this_mapping)
        # print("This mampping length", len(this_mapping))
        #print("going to next mapping")
        # for j in range(len(this_mapping)):
        #     dest_list = list(range(this_mapping[j][0],this_mapping[j][0]+this_mapping[j][2]))
        #     source_list = list(range(this_mapping[j][1],this_mapping[j][1]+this_mapping[j][2]))
        #     #print("DEST LIST", dest_list)
        #     #print("SOURCE LIST", source_list)

        #     # for k in range(len(dest_list)): #source and dest are the same length
        #     #     total_dest.append(dest_list[k])
        #     #     total_source.append(source_list[k])
        #     for r in range(len(dest_list)):
        #         #print(total_source[r], total_dest[r])
        #         if start_number == source_list[r]:
        #             start_number = dest_list[r]
        #             #print("NEW START NUMBER", start_number)
        #             i+=1
        #             j+=1
        #             break #break and go to next mapping
        #     else:
        #         continue
        #    break
        # for p in range(len(total_source)):
        #     print(total_source[p], total_dest[p])
    print("Location: ",start_number)
    return start_number

with open(file_name) as f:
    lines = f.readlines()

    #first line are the seeds
    seeds_txt = lines[0].split(":")[1].split()
    seeds_number = [int(i) for i in seeds_txt]

    all_seeds = []
    for i in range(0,len(seeds_number),2):
        all_seeds.extend(list(range(seeds_number[i], seeds_number[i] + seeds_number[i+1])))

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

    #have to divide into lowest location
    locations = []
    for i in range(len(all_seeds)):
        location = get_location(all_seeds[i], total_mapping_list)
        locations.append(location)

    print(locations)
    print("Lowest location", min(locations))

