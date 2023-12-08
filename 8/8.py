import re
inp = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".splitlines()

inp = open("input.txt").read().splitlines()

instructions_counter=0
instructions = re.findall(r"[R|L]",inp.pop(0))
inp.pop(0)

mapping = {}

for line in inp:
    threeStrings = re.findall(r"\w{3}",line)
    mapping[threeStrings[0]] = (threeStrings[1],threeStrings[2])

print(mapping)

moves = 0
start = "AAA"

while start != "ZZZ":
    if instructions[instructions_counter] == "L":
        start = mapping[start][0]
    else:
        start = mapping[start][1]
    moves+=1
    instructions_counter += 1
    instructions_counter %= len(instructions)
print(moves)