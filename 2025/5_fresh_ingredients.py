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

def part2():
    file_name = "5_input_test.txt"
    ranges, ingredients = read_ingredient_file(file_name)
    print(ranges)
    ranges.sort
    print(ranges)
    #fresh_ingredients = len(combined_ranges)
    #print("Combined ranges:", combined_ranges)
    #print("Number of fresh ingredients:", fresh_ingredients)

if __name__ == "__main__":
    #part1()
    part2()