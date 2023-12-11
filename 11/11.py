inp = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

inp = open("input.txt").read()

inp = inp.splitlines()



# EXPAND
emptyrows = []
for row in range(len(inp)):
    line = inp[row]
    if "#" not in line:
        emptyrows.append(row)
for i,row in enumerate(emptyrows):
    inp.insert(row+i,"."*len(inp[0]))

emptycolumns = []
for column in range(len(inp[0])):
    temp=""
    for row in range(len(inp)):
        temp += inp[row][column]
    if "#" not in temp:
        emptycolumns.append(column)
for j, column in enumerate(emptycolumns):
    for row in range(len(inp)):
        temp = list(inp[row])
        temp.insert(column+j,".")
        inp[row] = "".join(temp)

print("\n".join(inp))

locations = []
for row in range(len(inp)):
    for column in range(len(inp[0])):
        if inp[row][column] == "#":
            locations.append((row,column))


count = 0
for i, startcoord in enumerate(locations):
    for destcoord in locations[i:]:
        dist  = abs(destcoord[0]-startcoord[0]) + abs(destcoord[1]-startcoord[1])
        count += dist
print(count)
