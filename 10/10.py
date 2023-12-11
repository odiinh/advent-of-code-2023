# inp = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""

# inp = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ..."""

inp = open("input.txt").read()

inp = inp.splitlines()

# Find S
y = 0
x = 0
for row in range(len(inp)):
    column = inp[row].find("S")
    if column != -1:
        y = row
        x = column
        break

# Validity Rules:
v_rules = {
    "|": {  
        "n": ["|", "F", "7","S"],
        "s": ["|", "L", "J","S"],
        "e": [],
        "w": [],
    },
    "-": {  
        "n": [],
        "s": [],
        "e": ["-", "J", "7","S"],
        "w": ["-", "F", "L","S"],
    },
    "L" : {
        "n": ["|", "F", "7","S"],
        "s": [],
        "e": ["-", "J", "7","S"],
        "w": [],
    },
    "J" : {
        "n": ["|", "F", "7","S"],
        "s": [],
        "e": [],
        "w": ["-", "F", "L","S"],
    },
    "7": {
        "n": [],
        "s": ["|", "L", "J","S"],
        "e": [],
        "w": ["-", "F", "L","S"],
    },
    "F": {
        "n": [],
        "s": ["|", "L", "J","S"],
        "e": ["-", "J", "7","S"],
        "w": [],
    },
    "S": {
        "n": ["|", "F", "7","S"],
        "s": ["|", "L", "J","S"],
        "e": ["-", "J", "7","S"],
        "w": ["-", "F", "L","S"],
    }

}



def traceLoop(y,x,yprev,xprev): # yes, i know i could do it recursivly; but it's christmas.
    print(inp[y][x])
    steps = 1 
    while inp[y][x] != "S":
        if y-1 >= 0:
            if inp[y-1][x] in v_rules[inp[y][x]]["n"] and (y-1 != yprev or x != xprev):
                yprev = y
                xprev = x
                y = y-1
                x = x
                steps +=1
                print(inp[y][x],y,x)
                continue
        if y+1 <= len(inp)-1:
            if inp[y+1][x] in v_rules[inp[y][x]]["s"] and (y+1 != yprev or x != xprev):
                yprev = y
                xprev = x
                y = y+1
                x = x
                steps +=1
                print(inp[y][x],y,x)
                continue
        if x+1 <= len(inp[0])-1:
            if inp[y][x+1] in v_rules[inp[y][x]]["e"] and (y != yprev or x+1 != xprev):
                yprev = y
                xprev = x
                y = y
                x = x+1
                steps +=1
                print(inp[y][x],y,x)
                continue
        if x-1 >= 0:
            if inp[y][x-1] in v_rules[inp[y][x]]["w"] and (y != yprev or x-1 != xprev):
                yprev = y
                xprev = x
                y = y
                x = x-1
                steps +=1
                print(inp[y][x],y,x)
                continue
        pass
    print(int(steps/2))
            





if inp[y-1][x] in v_rules[inp[y][x]]["n"]:
    print("Start by looking north")
    traceLoop(y-1,x, y,x)
elif inp[y+1][x] in v_rules[inp[y][x]]["s"]:
    print("Start by looking south")
    traceLoop(y+1,x, y,x)
elif inp[y][x+1] in v_rules[inp[y][x]]["e"]:
    print("Start by looking east")
    traceLoop(y,x+1, y,x)
elif inp[y][x-1] in v_rules[inp[y][x]]["w"]:
    print("Start by looking west")
    traceLoop(y,x-1, y,x)


