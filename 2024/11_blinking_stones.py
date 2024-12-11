import time 
test_input = "125 17"
real_input = "0 7 6618216 26481 885 42 202642 8791"

start_time = time.time()
stone_list = real_input.split()
stone_list = [int(i) for i in stone_list] #make it to numbers

def blinking_stones(stone_list,blinks):
    blink_counter = 0
    while blink_counter < blinks:
        new_stone_list = [] #add tuple with index and number
        for i in range(len(stone_list)):
            if stone_list[i] == 0:
                stone_list[i] = 1
            elif len(str(stone_list[i])) % 2 == 0: #if it is an even number
                half_way = int(len(str(stone_list[i]))/2)
                new_stone_list.append((i,int(str(stone_list[i])[half_way:half_way*2]))) #cant add it to the stone list until all stones have been changes to be appended after the i
                stone_list[i] = int(str(stone_list[i])[0:half_way]) #then change the stone
            else:
                stone_list[i] = stone_list[i] * 2024
        #add the new stones
        #obs index saved is based on the original stone list, so if stones are added we also have to add that to the index
        items_inserted = 0
        for new_stone in new_stone_list:
            stone_list.insert(new_stone[0]+1+items_inserted,new_stone[1])
            items_inserted += 1
        #print("Stone list after blink number", blink_counter)
        #print(stone_list)

        #only add the new stones after you have gone through all stones
        blink_counter += 1
    print("Length of stone list:", len(stone_list))

blinking_stones(stone_list,25)
print("Process finished --- %s seconds ---" % (time.time() - start_time))
