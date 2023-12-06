import re
inp = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

inp = open("input.txt").read().splitlines()

times = [int(i) for i in re.findall(r"\d+",inp[0])]
distances = [int(i) for i in re.findall(r"\d+", inp[1])]

prod = 1

for i in range(len(times)):
    maxTime = times[i]
    targetDistance = distances[i]
    holdTimes = 0
    for t in range(1,maxTime):
        distance = t * (maxTime-t)
        if distance > targetDistance:
            holdTimes += 1
    prod *= holdTimes
print(prod)