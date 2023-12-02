import re

inp = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

inp = open("input.txt").read().splitlines()

limits = {"red": 12, "green": 13, "blue": 14}

valids = []

games = {}

for line in inp:
    print(line)
    valid = True
    game_number = re.search(r"\d+(?=:)",str(line)).group()
    for key in limits.keys():
        colour_search = re.findall(r"\d+(?= " + key+ r")", line)
        for num in colour_search:
            if int(num) > limits[key]:
                valid = False
    if valid == True:
        valids.append(int(game_number))
print(sum(valids))
        