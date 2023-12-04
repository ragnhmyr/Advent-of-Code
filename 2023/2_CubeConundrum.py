#Part 1 & 2

valid_ids = []
powers = []
game_dict = {"red": 12, "green": 13, "blue": 14}

def check_cubes(game_dict, number, color):
    if color not in game_dict.keys():
        return 1
    elif color in game_dict.keys():
        if number > game_dict[color]: 
            return 1
    return 0

with open('2_input.txt') as f:
    for line in f:
        gameId = int(line.split(":")[0].split()[1]) #get gameId
        each_set = line.split(":")[1].split(";")
        invalid_set = 0 #set to true until proven false
        max_color = {"red": 0, "green": 0, "blue": 0}
        for item in each_set:
            if item:
                each_color = item.split(",") #remove trailing space and separate colours
                for color in each_color:
                    if color:
                        number_color = color.strip().split() #remove trailing space and \n and split into number and color
                        number = int(number_color[0])
                        color = number_color[1]
                        invalid_set += check_cubes(game_dict, number, color)
                        if number > max_color[color]:
                            max_color[color] = number
        if invalid_set == 0:
            valid_ids.append(gameId)
        power = 1
        for color in max_color:
            power = power*max_color[color]
        powers.append(power)

print("Sum ids of possible games", sum(valid_ids))

print("Sum of powers", sum(powers))
