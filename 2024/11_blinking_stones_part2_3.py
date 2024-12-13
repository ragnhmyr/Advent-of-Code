from collections import defaultdict
from collections import Counter
import time 

test_input = "125 17"  # Should be 22 stones after 6 blinkings
real_input = "0 7 6618216 26481 885 42 202642 8791"

start_time = time.time()
stone_list = list(map(int, real_input.split()))  # Convert strings to integers
print(stone_list)

def count_stones(stone_counts, blinks):
    for _ in range(blinks):
        new_counts = defaultdict(int)
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                mid = len(str(stone)) // 2
                left = int(str(stone)[:mid])
                right = int(str(stone)[mid:])
                new_counts[left] += count
                new_counts[right] += count
            else:
                new_stone = stone * 2024
                new_counts[new_stone] += count
        stone_counts = new_counts
    return sum(stone_counts.values())

# Initial stones as a dictionary with counts
# initial_stones = {125: 1, 17: 1}
initial_stones = Counter(stone_list)
print(initial_stones)

# Calculate number of stones after 75 blinks
result = count_stones(initial_stones, 75)  # Use 6 blinks for testing
print(result)
print("Process finished --- %s seconds ---" % (time.time() - start_time))