time = [47,98,66,98] #how long the race lasts
distance = [400,1213,1011,1540] #distance you have to beat

time = [47986698]
distance = [400121310111540]

def possible_wins(time, distance):
    possible_solution = 0
    #print("TOTAL TIME", time, "DISTANCE", distance)
    for button_holding_time in range(time+1):
        speed = button_holding_time
        moving_time = time - button_holding_time
        distance_moved = moving_time * speed
        if distance_moved > distance:
            possible_solution += 1
            #print("speed: ", speed, "holding_time:", button_holding_time, "moving_time: ", moving_time, "distance_moved: ", distance_moved)
    return possible_solution

solutions = []

for i in range(len(time)):
    solutions.append(possible_wins(time[i], distance[i]))

print(solutions)

error_margin = 1
for number in solutions:
    error_margin = number * error_margin

print(error_margin)