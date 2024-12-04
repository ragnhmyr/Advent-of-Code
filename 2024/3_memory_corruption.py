import re
text = ""
with open('3_input.txt') as f:
    text = f.read()

max_length = len(text)
print("Max length: ", max_length)

#part 1
# multiplied = []
# get_all_mul = re.findall(r"mul\((\d{1,3},\d{1,3})\)", text)
# for item in get_all_mul:
#     numbers = item.split(",")
#     print(numbers)
#     multiplied.append(int(numbers[0])*int(numbers[1]))
# print("Sum multiplication: ", sum(multiplied))

#check when to multiply and when to not 
#if there is a last to, add max length as index
def get_dos(dos,donts,max_length):
    dos_starts = [0] # start of the do span
    donts_starts = []
    print(donts)
    for item in donts:
        donts_starts.append(item.start())
    for item in dos:
        dos_starts.append(item.start())
    start_do_span = 0
    end_do_span = 1
    do_spans = []
    # print("DOS START", dos_starts)
    # print("DONTS START", donts_starts)
    for start in dos_starts:
        # Find the first `dont` start that comes after this `do` start
        end_do_span = max_length  # Default to max_length
        for dont in donts_starts:
            if dont > start:
                end_do_span = dont
                break  # Stop as soon as we find the nearest `dont`
        
        do_spans.append((start, end_do_span))
    #print(do_spans)
    return do_spans

#part 2
multiplied = []
get_all_mul = re.finditer(r"mul\((\d{1,3},\d{1,3})\)", text)
#find the indexes of the dos and donts 
dos = re.finditer(r"do\(\)", text)
dont = re.finditer(r"don't\(\)", text)
# for item in get_all_mul:
#     numbers = item.split(",")
#     print(numbers)
#     multiplied.append(int(numbers[0])*int(numbers[1]))


do_spans = get_dos(dos,dont,max_length)
print("DO SPANS", do_spans)

for item in get_all_mul:
    start_item = item.start()
    print("Checking item: ", item)
    print("It starts at: ", start_item)
    #check if start exist in one of the dos - ranges
    #could also do a loop and just check for one true
    to_multiply = [start_item >= r0 and start_item <= r1 for r0, r1 in do_spans]
    print("Does it exist in: ", to_multiply)
    if any(to_multiply) == True:
        numbers = item.group().split(",")
        digits = re.findall(r'\s*(\d+)\s*', item.group())
        #print("THIS IS THE DIGITS: ", digits)
        multiplied.append(int(digits[0])*int(digits[1]))

#for item in get_all_mul:
    #print("item: ", item)
    #span = item.span()
    #print("span: ", span)
#print(multiplied)
print("Sum multiplication: ", sum(multiplied))

# before I understood it had to be 1-3 digits with a comma in between, not any other symbols within the mul()
# so this was a bit overcomplicated
# get_all_mul = re.findall(r"mul\((.*?)\)", text)
# multiplied_numbers = []
# #get_all_mul = re.finditer(r"mul\((.*?)\)", text)
# for item in get_all_mul:
#     #digits = re.findall(r"\d*(\,)*\d", item)
#     print("this is the item: ", item)
#     digits = re.findall(r'\s*(\d+)\s*', item)
#     if len(digits) == 2:
#         multiplied_numbers.append(int(digits[0]) * int(digits[1]))
#     else: #check again, it might be that a mul(*) is inside another mul()
#         #check2 = re.findall(r'mul\((\d+,\d+)$', item)
#         check2 = re.findall(r'mul\((\d+),(\d+)', item)
#         print("this is the check2", check2)
#         if check2:  # Ensure there's at least one match
#             # Access the first tuple and unpack it
#             print("Check 2 true")
#             first_num, second_num = check2[0]
#             print("first_num: ", first_num, "second_num: ", second_num)
#             multiplied_numbers.append(int(first_num) * int(second_num))

# #then return the two two numbers
# #print("multiplied numbers: ", multiplied_numbers)   
# print("Sum multiplication: ", sum(multiplied_numbers))
# #one boundary case itentified: mul(32,64]then(mul(11,8)mul(8,5))