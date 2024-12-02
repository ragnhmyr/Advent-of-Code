list_1 = []
list_2 = []
with open('1_input.txt') as f:
    for line in f:
        this_line = line.split()
        list_1.append(int(this_line[0]))
        list_2.append(int(this_line[1]))

#part 1
    
#sort the lists 
list_1.sort()
list_2.sort()
distances = []
for i in range(len(list_1)):
    distances.append(abs(list_1[i] - list_2[i]))
    
print("Sum distance: ", sum(distances))

#part 2 
#could optimise by only checking from the last index of the last occurence
occurences = []
for number in list_1:
    this_occurence = 0
    for j in range(len(list_2)):
        if list_2[j] == number:
            this_occurence += 1
        if list_2[j] > number:
            break
    occurences.append(this_occurence*number)

#print("Occurences: ", occurences)
print("Sum occurences: ", sum(occurences))
    
#occurences.append(list_1.count(list_2[i]))
