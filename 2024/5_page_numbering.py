page_dict = {}#
ordering_list = []
with open('5_input.txt') as f:
    for line in f:
        this_line = line.strip()
        if ("|" in this_line):
            first,second = this_line.split("|") #can only be two numbers
            first = int(first)
            second = int(second)
            if first in page_dict:
                page_dict[first].append(second)
            else:
                page_dict[first] = [second]
        # requires that noe ordering contains only one page number (thats what it looks like in the input)    
        elif ("," in this_line):
            ordering = this_line.split(",")
            #make it to numbers instead of strings
            ordering = [int(x) for x in ordering]
            ordering_list.append(ordering)
#now check the ordering 
print("This is the page dict", page_dict)
#print("This is the ordering list", ordering_list)
correct_ordering = 0
#must check both forward and backward in list
medians_in_list = []
wrong_lists = []
for list in ordering_list:
    #print("This is the list", list)
    this_list_order = True
    #if list order still is true we add the median value to the median list
    # check just backwards, from the end. that the numbers before are not in the page dict
    for i in range(len(list)-1,0,-1):
        if list[i] in page_dict:
            for j in range(i):
                if list[j] in page_dict[list[i]]:
                    this_list_order = False
                    break
    #assume that all lengths are odd numbers, which they must be if there is a middle value
    if this_list_order:
        medians_in_list.append(list[len(list)//2]) #// is floor division
    else:
        wrong_lists.append(list)

print("Part 1: Median in list", medians_in_list)
print("Part 1: Sum of medians", sum(medians_in_list))
print("Part 1: Wrong lists", wrong_lists)

medians_part_2 = []
#Part 2: Order the wrong lists
for list in wrong_lists:
    #check if the list is in the wrong order
    print("Looking at list", list)  
    for i in range(len(list)-1,0,-1):
        print("Looking at number", list[i])
        if list[i] in page_dict:
            print("The number is in the page dict")
            for j in range(i):
                if list[i] in page_dict: # have to check again since the list might have been changed
                    if list[j] in page_dict[list[i]]:
                        #switch the two numbers
                        print(list[j], "is in the page dict of", list[i])
                        print("Swiching", list[i], "and", list[j])
                        list[i], list[j] = list[j], list[i]
                        print("This is the new list", list)
    medians_part_2.append(list[len(list)//2]) #then the list is correctly sorted
    print("This is the new ordered list", list)

#4667 was too low - had a break so only did one switch and then stopped
print("Part 2: Median in list", medians_part_2)
print("Part 2: Sum of medians", sum(medians_part_2))