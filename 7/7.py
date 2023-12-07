import re
from collections import Counter
inp = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

inp = open("index.txt").read()

hands = re.findall(r"\S{5}", inp)
bids = [int(i) for i in re.findall(r"(?<= )\d{1,4}", inp)]


cardTypes = {
    "A" : 14,
    "K" : 13,
    "Q" : 12,
    "J" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
}

handRankings = {i:[] for i in range(7)}
# 0: five of a kind
# 1: four of a kind
# 2: full house
# 3: three of a kind
# 4: two pair
# 5: one pair
# 6: high card

def place(hand, index,bid):
    current = handRankings[index]
    cardorder = list(cardTypes.keys())
    if current == []:
        current = [[hand,bid]]
    else:
        i = 0
        compareindex = 0
        startinglength = len(current)
        while True:
            a = cardorder.index(hand[compareindex])
            b = cardorder.index(current[i][0][compareindex])
            if a == b:
                compareindex+=1
            elif a<b:
                current.insert(i,[hand,bid])
                break
            elif a>b:
                i+=1
                compareindex = 0
                if i == len(current):
                    current.append([hand,bid])
                    break
    handRankings[index] = current

for i in range(len(hands)):
    hand = hands[i]
    bid = bids[i]
    counter = Counter(hand)
    counts = list(counter.values())
    if len(counter) == 1:
        place(hand, 0,bid)
    elif counts.count(4) == 1:
        place(hand, 1,bid)
    elif counts.count(3) == 1 and len(counter) == 2:
        place(hand, 2,bid)   
    elif counts.count(3) == 1 and len(counter) == 3:
        place(hand, 3,bid)
    elif counts.count(2) == 2:
        place(hand, 4,bid)
    elif counts.count(2) == 1:
        place(hand, 5,bid)
    else:
        place(hand, 6,bid)
        

orderedList = []
for ranking in list(reversed(handRankings.values())):
    orderedList += (list(reversed(ranking)))



winnings = 0
for i in range(1, len(orderedList)+1):
    print(i)
    winnings += (i * orderedList[i-1][1])
    
print(winnings)
