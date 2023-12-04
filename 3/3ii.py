import re
from numpy import prod
# inp = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..""".splitlines()

inp = open("input.txt").read().splitlines()

cog_dict = {}

def checkandadd(y,x,num):
    if inp[y][x] == "*":
        current_value = cog_dict.get((y,x),[])
        current_value.append(int(num))
        cog_dict[(y,x)] = current_value
        
ratio_sum=0

print("  l,   bl,  b,   t,   tr,  tl,  br,  r")
for i in range(len(inp)):
    current_line = inp[i]
    matches = re.finditer(r"\d{1,3}",current_line)
    for match in matches:
        num = match.group()
        start = match.start()
        end = match.end()-1
        adjacents = []
        if start-1 >=0:
            checkandadd(i,start-1,num) # left
            if i+1!=len(inp):
                checkandadd(i+1,start-1,num) # bottom left
        
        if i+1!=len(inp):
            [checkandadd(i+1,j,num) for j in range(start,end+1)] # bottom directly

        if i-1 >=0:
            [checkandadd(i-1,j,num) for j in range(start,end+1)] # top directly
            if end+1 != len(current_line):
                checkandadd(i-1,end+1,num) # top right
            if start-1 >=0:
                checkandadd(i-1,start-1,num) # top left
                
        if end+1 != len(current_line):
            if i+1!=len(inp):
                checkandadd(i+1,end+1,num) # bottom right
            checkandadd(i,end+1,num) # right

for value in cog_dict.values():
    if len(value) == 2:
        ratio_sum += prod(value)

print(ratio_sum)

