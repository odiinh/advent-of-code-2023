import re
import math
inp = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)""".splitlines()

inp = open("input.txt").read().splitlines()

instructions_counter=0
instructions = re.findall(r"[R|L]",inp.pop(0))
inp.pop(0)

mapping = {}

for line in inp:
    threeStrings = re.findall(r"\w{3}",line)
    mapping[threeStrings[0]] = (threeStrings[1],threeStrings[2])

starts = [i for i in mapping.keys() if i.endswith("A") == True]

allendwithZ = False


for i in range(len(starts)):
    moves = 0
    start = starts[i]
    while start.endswith("Z") == False:
        if instructions[instructions_counter] == "L":
            start = mapping[start][0]
        else:
            start = mapping[start][1]
        moves+=1
        instructions_counter += 1
        instructions_counter %= len(instructions)
    starts[i] = moves
while len(starts) != 1:
    starts.insert(0,math.lcm(starts.pop(0),starts.pop(0)))
print(starts)