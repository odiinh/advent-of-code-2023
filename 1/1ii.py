inp = open("input.txt").read().split("\n")

# inp = """
# eightthree8fiveqjgsdzgnnineeight
# 1a9""".split("\n")

a = {   "one":1,
        "two":2,
        "three":3,
        "four": 4,
        "five": 5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
        }

b = 0

for line in inp:
    firstnumberindex = float("inf")
    firstnumber = 0
    lastnumberindex = float("-inf")
    lastnumber = 0
    for i in line:
        if i.isnumeric():
            if (line.index(i) < firstnumberindex):
                firstnumberindex = line.index(i)
                firstnumber = int(i)

    for key in a.keys():
        try:
            if line.index(key) < firstnumberindex:
                firstnumberindex = line.index(key)
                firstnumber = a[key]
        except:
            continue
    for i in line:
        if i.isnumeric():
            if (line.rindex(i) > lastnumberindex):
                lastnumberindex = line.rindex(i)
                lastnumber = int(i)

    for key in a.keys():
        try:
            if line.rindex(key) > lastnumberindex:
                lastnumberindex = line.rindex(key)
                lastnumber = a[key]
        except:
            continue
    print(line,firstnumber,lastnumber)
    b+=firstnumber*10
    b+=lastnumber
    
print(b)