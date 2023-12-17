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
            return calculate_value(allNumbers) 
        # if sum(allNumbers[index]) == 0:
        #     allZeros = True
        #     return calculate_value(allNumbers)    
    return 0

def calculate_value(allNumbers):
    value = 0
    for i in range(len(allNumbers)):
        value += allNumbers[i][-1]
    return value

with open(file_name) as f:
    lines = f.readlines()
    total = 0
    for i in range(len(lines)):
        value = get_history_value(lines[i])
        total+=value
    print(total)

#1939607041 var for høyt
#1939607039 funker