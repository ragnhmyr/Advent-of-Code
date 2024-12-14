from sympy import symbols, Eq, solve, S
import time

def parse_file(filename, part2=False):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    parsed_data = []
    temp = {}
    for line in lines:
        line = line.strip()
        if line.startswith("Button A"): 
            x_a = int(line.split('X+')[1].split(',')[0])
            y_a = int(line.split('Y+')[1])
            temp['a'] = (x_a, y_a)
        elif line.startswith("Button B"):
            x_b = int(line.split('X+')[1].split(',')[0])
            y_b = int(line.split('Y+')[1])
            temp['b'] = (x_b, y_b)
        elif line.startswith("Prize"):
            prize_x = int(line.split('X=')[1].split(',')[0])
            prize_y = int(line.split('Y=')[1])
            if part2:
                prize_x += 10000000000000
                prize_y += 10000000000000
            temp['prize'] = (prize_x, prize_y)
            parsed_data.append(temp)
            temp = {}
    return parsed_data

def solve_equations(data, part2=False):
    a, b = symbols('a b', integer=True)
    total_min_tokens = 0
    for entry in data:
        x_a, y_a = entry['a']
        x_b, y_b = entry['b']
        prize_x, prize_y = entry['prize']

        equations = [Eq(x_a * a + x_b * b, prize_x), Eq(y_a * a + y_b * b, prize_y)]
        result = solve(equations, (a, b), dict=True)
        #filtered_result = [res for res in result if 0 <= res[a] <= 100 and 0 <= res[b] <= 100]
        if not part2:
            result = [res for res in result if 0 <= res[a] <= 100 and 0 <= res[b] <= 100] #part 1 check a and be  between 0 and 100
        print(f"Filtered Solution: {result}\n")

        min_tokens = get_minimum_tokens(result, a, b)
        total_min_tokens += min_tokens
    return total_min_tokens

def get_minimum_tokens(eq_result, a, b):
    price_a = 3
    price_b = 1
    if len(eq_result) == 0:
        return 0
    elif len(eq_result) == 1:
        return eq_result[0][a]*price_a + eq_result[0][b]*price_b
    #more than one solution, need to find minimum
    else:
        #min_tokens = 100*price_a + 100*price_b #max possible tokens
        min_tokens = float('inf')
        for result in eq_result:
            tokens = result[a]*price_a + result[b]*price_b
            if tokens < min_tokens:
                min_tokens = tokens
        return min_tokens

if __name__ == "__main__":
    start_time = time.time()
    filename = "13_input.txt" 
    part2 = True
    data = parse_file(filename, part2=part2)
    total_min_tokens = solve_equations(data, part2=part2)
    end_time = time.time()
    print(f"Total Minimum Tokens: {total_min_tokens}")
    print(f"Execution Time: {end_time - start_time:.2f} seconds")