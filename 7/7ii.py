import re
from collections import Counter
inp = """JJJJJ 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

inp = open("index.txt").read()

hands = re.findall(r"\S{5}", inp)
bids = [int(i) for i in re.findall(r"(?<= )\d{1,4}", inp)]


cardTypes = {
    "A" : 13,
    "K" : 12,
    "Q" : 11,
    "T" : 10,
    "9" : 9,
    "8" : 8,
    "7" : 7,
    "6" : 6,
    "5" : 5,
    "4" : 4,
    "3" : 3,
    "2" : 2,
    "J" : 1,
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
    cards = list(counter.keys())
    counts = list(counter.values())
    if "J" in cards: # separated for debugging purposes
        if (len(counter) <= 2):
            place(hand, 0,bid) # five of a kind
        elif (len(counter) == 3) and (max(counts) == 3 or counter["J"]>1):
            place(hand, 1,bid) # four of a kind
        elif (counts.count(2) == 2 and max(counts) == 2):
            place(hand, 2,bid) # full house (three and a pair)
        elif (counts.count(2) == 1):
            place(hand, 3,bid) # three of a kind 
        else:
            place(hand, 5,bid) # one pair

    else:
        if len(counter) == 1:
            place(hand, 0,bid) # five of a kind
        elif counts.count(4) == 1:
            place(hand, 1,bid) # four of a kind
        elif (counts.count(3) == 1 and len(counter) == 2):
            place(hand, 2,bid) # full house (three and a pair)
        elif (counts.count(3) == 1 and len(counter) == 3):
            place(hand, 3,bid) # three of a kind 
        elif counts.count(2) == 2:
            place(hand, 4,bid) # two pair
        elif counts.count(2) == 1:
            place(hand, 5,bid) # one pair
        else:
            place(hand, 6,bid) # high card
        

orderedList = []
for ranking in list(reversed(handRankings.values())):
    orderedList += (list(reversed(ranking)))



winnings = 0
for i in range(1, len(orderedList)+1):
    winnings += (i * orderedList[i-1][1])

# print(handRankings)
print(winnings)
