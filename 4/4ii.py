import re

# inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11""".splitlines()

inp = open("input.txt").read().splitlines()

totals = {i:1 for i in range(1,len(inp)+1)}

for key in totals.keys():
    line = inp[key-1].replace(":","|").split("|")
    card_no = int(re.findall(r"\d{1,3}",line[0])[0])
    winners = [int(i.group()) for i in re.finditer(r"\d{1,2}",line[1])]
    cardnumbers = [int(i.group()) for i in re.finditer(r"\d{1,2}",line[2])]
    howmanynext = 1
    for number in cardnumbers:
        if number in winners:
            totals[key+howmanynext] += 1*totals[key]
            howmanynext +=1
            
print(sum(totals.values()))