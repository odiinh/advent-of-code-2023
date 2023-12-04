import re

inp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()

# inp = open("input.txt").read().splitlines()

part_numbers = []

for i in range(len(inp)):
    current_line = inp[i]
    matches = re.finditer(r"\d{1,3}",current_line)
    for match in matches:
        num = match.group()
        start = match.start()
        end = match.end()-1
        adjacents = []
        if start-1 >=0:
            adjacents.append(current_line[start-1]) # left
            if i+1!=len(inp):
                adjacents.append(inp[i+1][start-1]) # bottom left
        
        if i+1!=len(inp):
            adjacents+=[inp[i+1][j] for j in range(start,end+1)] # bottom directly

        if i-1 >=0:
            adjacents+=[inp[i-1][j] for j in range(start,end+1)] # top directly
            if end+1 != len(current_line):
                adjacents.append(inp[i-1][end+1]) # top right
            if start-1 >=0:
                adjacents.append(inp[i-1][start-1]) # top left
                
        if end+1 != len(current_line):
            if i+1!=len(inp):
                adjacents.append(inp[i+1][end+1]) # bottom right
            adjacents.append(current_line[end+1]) # right
        print(adjacents)
        for adjacent in adjacents:
            if adjacent in ['+', '%', '*', '$', '&', '#', '@', '=', '-', '/']:
                part_numbers.append(int(num))
print(sum(part_numbers))

