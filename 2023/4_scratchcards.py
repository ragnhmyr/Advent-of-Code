import re

file_name = '4_input.txt'

#PART 1
sum_each_game = []
with open(file_name) as f:
    for line in f:
        this_game = 0
        winning_text = line.split("|")[0].split(":")[1].strip()
        your_text = line.split("|")[1].strip()
        winning_numbers = re.findall("\d+", winning_text)
        your_numbers = re.findall("\d+", your_text)
        for any_number in your_numbers:
            if any_number in winning_numbers:
                if this_game==0:
                    this_game = 1
                else:
                    this_game *= 2
        sum_each_game.append(this_game)

print(sum(sum_each_game))

#PART 2

def process_scratchcards(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    # Initialize copies with 1 for each original card
    copies = [1] * len(lines)

    # Iterate over each card and its copies
    for i, line in enumerate(lines):
        winning_text = line.split("|")[0].split(":")[1].strip()
        your_text = line.split("|")[1].strip()
        winning_numbers = re.findall("\d+", winning_text)
        your_numbers = re.findall("\d+", your_text)

        matches = sum(num in winning_numbers for num in your_numbers)
        # Add copies to subsequent cards based on the number of matches
        for j in range(i + 1, min(i + 1 + matches, len(lines))):
            copies[j] += copies[i]

    return sum(copies)

total_scratchcards = process_scratchcards(file_name)
print("Total scratchcards:", total_scratchcards) 