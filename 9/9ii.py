inp = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

inp = open("input.txt").read().splitlines()


total = 0

for a in range(len(inp)):
    diffs = [[int(j) for j in inp[a].split()]]
    while set(diffs[-1]) != {0}:
        newdiffs = []
        copy = diffs[-1].copy()
        for i in range(len(copy) - 1):
            difference = copy[i + 1] - copy[i]
            newdiffs.append(difference)
        diffs.append(newdiffs)
    ### extrapolate
    for b in range(len(diffs)-2,-1,-1):
        diffs[b].insert(0,diffs[b][0]-diffs[b+1][0])
    total+=diffs[0][0]
print(total)
