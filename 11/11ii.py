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

emptycolumns = []
for column in range(len(inp[0])):
    temp=""
    for row in range(len(inp)):
        temp += inp[row][column]
    if "#" not in temp:
        emptycolumns.append(column)

locations = []
for row in range(len(inp)):
    for column in range(len(inp[0])):
        if inp[row][column] == "#":
            locations.append((row,column))


count = 0
for i, startcoord in enumerate(locations):
    for destcoord in locations[i:]:
        dist = 0
        for row in emptyrows:
            if row in range(startcoord[0],destcoord[0]) or row in range(destcoord[0],startcoord[0]):
                dist+=999_999
        for column in emptycolumns:
            if column in range(startcoord[1],destcoord[1]) or column in range(destcoord[1],startcoord[1]):
                dist+=999_999
        dist += abs(destcoord[0]-startcoord[0]) + abs(destcoord[1]-startcoord[1])
        
        count += dist
print(count)
