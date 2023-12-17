file_name = "9_input.txt"

def get_history_value(line):
    string = line.strip().split()
    startNumbers = [int(x) for x in string]
    allZeros = False
    allNumbers = [startNumbers]
    index = 0
    while allZeros == False:
        newList = []
        for i in range(len(allNumbers[index])-1):
            newList.append(allNumbers[index][i+1]-allNumbers[index][i])
        allNumbers.append(newList)
        index += 1
        if len(set(allNumbers[index])) == 1: 
            allZeros = True
            return calculate_value_backwards(allNumbers)   
    return 0

#part 1
def calculate_value(allNumbers):
    value = 0
    for i in range(len(allNumbers)):
        value += allNumbers[i][-1]
    
    return value
#part 2
def calculate_value_backwards(allNumbers):
    start_list = [0]
    index = 0
    for i in range(len(allNumbers)-1, -1, -1):
        start_list.append(allNumbers[i][0] - start_list[index])
        index+=1
    return start_list[-1]
# -16823 feil

with open(file_name) as f:
    lines = f.readlines()
    total = 0
    for i in range(len(lines)):
        value = get_history_value(lines[i])
        total+=value
    print("TOTAL", total)

#1041 total