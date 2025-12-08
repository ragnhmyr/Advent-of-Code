def read_ingredient_file(filename: str):
    ranges = []
    lines = []
    ingredients = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    for line in lines:
        if "-" in line:
            parts = line.split("-")
            start = int(parts[0])
            end = int(parts[1]) + 1 # to include the end value
            ranges.append(range(start,end))
        elif len(line) > 0:
            ingredients.append(int(line))
    
    return ranges, ingredients

#takes too long on the proper input
def combine_ranges(ranges):
    combined = set()
    for r in ranges:
        combined.update(r)
    return combined

def part1():
    file_name = "5_input.txt"
    ranges, ingredients = read_ingredient_file(file_name)
    valid_ingredients = 0
    for ingredient in ingredients:
        for r in ranges:
            if ingredient in r:
                valid_ingredients += 1
                break
    print("Sum of valid ingredients:", valid_ingredients)

def merge_ranges(ranges):
    if not ranges:
        return []

    # Sort by starting value
    ranges = sorted(ranges, key=lambda r: r.start)

    merged = []
    current_start = ranges[0].start
    current_stop = ranges[0].stop 

    for r in ranges[1:]:
        start, stop = r.start, r.stop

        if start <= current_stop:  
            # Overlapping or touching (depending on your definition)
            # Extend the current range
            if stop > current_stop:
                current_stop = stop
        else:
            # No overlap: push the previous merged range and start a new one
            merged.append(range(current_start, current_stop))
            current_start, current_stop = start, stop

    # Add the last range
    merged.append(range(current_start, current_stop))
    return merged

def part2():
    file_name = "5_input.txt"
    ranges, ingredients = read_ingredient_file(file_name)
    #combined_ranges = combine_ranges(ranges)
    merged_ranges = merge_ranges(ranges)
    #print("Merged ranges", merged_ranges)
    #print("Combined ranges:", combined_ranges)
    fresh_ingredients = 0
    for r in merged_ranges:
        fresh_ingredients += len(r)
    print("Number of fresh ingredients:", fresh_ingredients)

if __name__ == "__main__":
    #part1()
    part2()