def read_file(filename: str):
    lines = []
    with open(filename, 'r') as file:
        lines = [(line.strip()) for line in file.readlines()]
    reactor_dict = {}
    for line in lines:
        start_split = line.split(": ")
        name_device = start_split[0]
        out_devices = start_split[1].split(" ")
        reactor_dict[name_device]=out_devices
    return reactor_dict

def traverse_dict(device,reactor_dict):
    count_paths = 0
    next_devices = reactor_dict[device]
    #print("Next devices ", next_devices)
    for this_device in next_devices:
        if this_device == "out":
            count_paths +=1
            #print("Found out")
        else:
            count_paths += traverse_dict(this_device,reactor_dict)
    return count_paths

def traverse_dict_part2(device,reactor_dict,passed_fft,passed_dac):
    count_paths = 0
    next_devices = reactor_dict[device]
    #print("Next devices ", next_devices)
    for this_device in next_devices:
        new_passed_fft = passed_fft or this_device == "fft"
        new_passed_dac = passed_dac or this_device == "dac"
        if this_device == "out":
            if passed_fft and passed_dac:
                count_paths += 1
        else:
            count_paths += traverse_dict_part2(this_device,reactor_dict,new_passed_fft,new_passed_dac)
    return count_paths

def part1():
    filename = "11_input.txt"
    reactor_dict = read_file(filename)
    print(reactor_dict)
    start_devices = reactor_dict['you']
    sum_paths = 0
    for device in start_devices:
        print(device)
        sum_paths+=traverse_dict(device,reactor_dict)
    print("Number of paths",sum_paths)

def part2():
    filename = "11_input.txt"
    reactor_dict = read_file(filename)
    #print(reactor_dict)
    start_devices = reactor_dict['svr']
    sum_paths = 0
    for device in start_devices:
        print(device)
        sum_paths+=traverse_dict_part2(device,reactor_dict,False,False)
    print("Number of paths",sum_paths)

if __name__ == "__main__":
    #part1()
    part2()