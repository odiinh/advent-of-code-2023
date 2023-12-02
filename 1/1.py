inp = open("input.txt").read().split("\n")

b=0
for line in inp:
    for i in line:
        if i.isnumeric():
            b+=int(i)*10
            break
    for i in reversed(line):
        if i.isnumeric():
            b+=int(i)
            break
print(b) 