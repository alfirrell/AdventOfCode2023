import numpy as np

#with open("2023/Day02/test_input.txt", "r") as f:
with open("2023/Day02/input_AJRF.txt", "r") as f:
    lines = f.read().splitlines() 

colour_dict = {"red": 12, "green": 13, "blue": 14}
success_games = []
for line in lines:
    game, draws = line.split(": ")
    game_id = int(game.replace("Game ", ""))

    under_threshold = True
    for draw in draws.split("; "):
        rgb = draw.split(", ")
        for colour_val in rgb:
            val, colour = colour_val.split(" ")
            val = int(val)
            threshold = colour_dict[colour]
            if val > threshold:
                under_threshold = False
                break
    if under_threshold:
        success_games.append(game_id)

np.sum(success_games)

# Part 2
powers = []
for line in lines:
    game, draws = line.split(": ")
    #game_id = int(game.replace("Game ", ""))

    max_vals = {"red": 0, "green": 0, "blue": 0}
    for draw in draws.split("; "):
        rgb = draw.split(", ")
        for colour_val in rgb:
            val, colour = colour_val.split(" ")
            val = int(val)
            if val > max_vals[colour]:
                max_vals[colour] = val
    power = np.product(list(max_vals.values())) 
    powers.append(power)
    
np.sum(powers)