import time 
from collections import Counter
test_input = "125 17" #should be 22 stones after 6 blinkings
real_input = "0 7 6618216 26481 885 42 202642 8791"

start_time = time.time()
stone_list = test_input.split()
stone_list = [int(i) for i in stone_list] #make it to numbers

#order in the stone list does not matter after all
def blinking_stones(stone_list,blinks,blink_counter=0, occurrences={}):
    if blink_counter == blinks:
        return stone_list,occurrences
    new_stone_list = [] 
    for i in range(len(stone_list)):
        if stone_list[i] == 0:
            stone_list[i] = 1
        elif len(str(stone_list[i])) % 2 == 0: #if it is an even number
            half_way = int(len(str(stone_list[i]))/2)
            new_stone_list.append((int(str(stone_list[i])[half_way:half_way*2]))) #cant add it to the stone list until all stones have been changes to be appended after the i
            stone_list[i] = int(str(stone_list[i])[0:half_way]) #then change the stone
        else:
            stone_list[i] = stone_list[i] * 2024
    stone_list.extend(new_stone_list)
    this_list_occurences = dict(Counter(stone_list))
    #update the occurences to add the new occurences
    for key in this_list_occurences:
        if key in occurrences:
            occurrences[key] += this_list_occurences[key]
        else:
            occurrences[key] = this_list_occurences[key]
    stone_list = list(set(stone_list)) #remove the duplicates
    blink_counter += 1
    return blinking_stones(stone_list,blinks,blink_counter, occurrences)


new_stone_list,all_occurences = blinking_stones(stone_list,6)
total_stones = 0
for key in all_occurences:
    total_stones += all_occurences[key]
print(new_stone_list)
print(all_occurences)
print("Total stones:", total_stones)
print("Process finished --- %s seconds ---" % (time.time() - start_time))