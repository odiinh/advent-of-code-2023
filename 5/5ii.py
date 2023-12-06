import concurrent.futures
import re
# inp = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

inp = open("input.txt").read()

seeds = [[int(j) for j in i.split(" ")] for i in re.findall(r"\d+ \d+",inp.splitlines()[0])]
print(seeds)
maps = {}

map_ranges = re.findall(r"(?<=map:\n)[\d+( |\n)]+", inp)
for i in range(len(map_ranges)):
    lst = maps.get(i,[])
    for j in map_ranges[i].strip().splitlines():
        lst.append(j.split(" "))
    maps[i] = lst

locations = []

pool = concurrent.futures.ThreadPoolExecutor(max_workers=1000)
def calculate(seedrange,maps):
    print(seedrange)
    lowest = float("inf")
    for seed in range(seedrange[0],seedrange[0]+seedrange[1]+1):
        i=0
        source = seed
        destination = seed
        while i != len(maps):
            for sd_map in maps[i]:
                if source >= int(sd_map[1]) and source<=int(sd_map[1])+int(sd_map[2]):
                    destination = source+(int(sd_map[0])-int(sd_map[1]))
                    break
            # print(source,destination)
            source = destination
            i+=1
        if destination < lowest:
            lowest = destination
    locations.append(lowest)
for seedrange in seeds:
    pool.submit(calculate,seedrange,maps) 
pool.shutdown(wait=True,cancel_futures=False)  
print(locations)
print(min(locations))







# while i != -1:
#     source = 0
#     destination = float("inf")
#     for sd_map in maps[i]:
#         if int(sd_map[0]) < destination:
#             source = int(sd_map[1])
#     destination = source
#     i-=1
#     for sd_map in maps[i]:
#         if destination >= int(map([0])) and destination <= int(map[0]) + int(map[2]):
#             source = destination - int()-int()
# for seedrange in seeds:
#     lowest = float("inf")
#     for seed in range(seedrange[0],seedrange[0]+seedrange[1]+1):
#         i=0
#         source = seed
#         destination = seed
#         while i != len(maps):
#             for sd_map in maps[i]:
#                 if source >= int(sd_map[1]) and source<=int(sd_map[1])+int(sd_map[2]):
#                     destination = source+(int(sd_map[0])-int(sd_map[1]))
#                     break
#             # print(source,destination)
#             source = destination
#             i+=1
#         if destination < lowest:
#             lowest = destination
#     locations.append(lowest)
# print(min(locations))

