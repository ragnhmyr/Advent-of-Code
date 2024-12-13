import time 
test_input = "125 17" #should be 22 stones after 6 blinkings
real_input = "0 7 6618216 26481 885 42 202642 8791"

start_time = time.time()
stone_list = real_input.split()
stone_list = [int(i) for i in stone_list] #make it to numbers

#could make it more effective by not checking same numbers several times but somehow save the amount of stones and how many more stones they make
def total_stones_for_a_number(number,blink_counter,max_blink):
    if blink_counter == max_blink:
        return 1
    if number == 0:
        return total_stones_for_a_number(1,blink_counter+1,max_blink)
    elif len(str(number)) % 2 == 0: #if it is an even number
        half_way = int(len(str(number))/2)
        new_number = int(str(number)[0:half_way])
        added_number = int(str(number)[half_way:half_way*2])
        return total_stones_for_a_number(new_number,blink_counter+1,max_blink) + total_stones_for_a_number(added_number,blink_counter+1,max_blink)
    else:
        return total_stones_for_a_number(number * 2024,blink_counter+1,max_blink)

total_stones = 0
for i in range(len(stone_list)):
    total_stones += total_stones_for_a_number(stone_list[i],0,25)
print(total_stones)

print("Process finished --- %s seconds ---" % (time.time() - start_time))